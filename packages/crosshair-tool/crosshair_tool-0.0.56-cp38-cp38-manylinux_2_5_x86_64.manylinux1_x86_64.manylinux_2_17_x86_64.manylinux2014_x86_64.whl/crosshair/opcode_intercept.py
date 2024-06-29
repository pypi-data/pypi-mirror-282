import dis
import sys
from collections.abc import MutableMapping, Set
from sys import version_info
from types import CodeType, FrameType
from typing import Callable

from crosshair.core import ATOMIC_IMMUTABLE_TYPES, CrossHairValue, register_opcode_patch
from crosshair.libimpl.builtinslib import (
    AnySymbolicStr,
    SymbolicBool,
    SymbolicInt,
    SymbolicList,
)
from crosshair.simplestructs import LinearSet, ShellMutableSet, SimpleDict, SliceView
from crosshair.tracers import (
    COMPOSITE_TRACER,
    NoTracing,
    TracingModule,
    frame_stack_read,
    frame_stack_write,
)
from crosshair.util import CrosshairInternal
from crosshair.z3util import z3Not

BINARY_SUBSCR = dis.opmap["BINARY_SUBSCR"]
BINARY_SLICE = dis.opmap.get("BINARY_SLICE", 256)
BUILD_STRING = dis.opmap["BUILD_STRING"]
COMPARE_OP = dis.opmap["COMPARE_OP"]
CONTAINS_OP = dis.opmap.get("CONTAINS_OP", 256)
FORMAT_VALUE = dis.opmap.get("FORMAT_VALUE", 256)
CONVERT_VALUE = dis.opmap.get("CONVERT_VALUE", 256)
MAP_ADD = dis.opmap["MAP_ADD"]
SET_ADD = dis.opmap["SET_ADD"]
UNARY_NOT = dis.opmap["UNARY_NOT"]
TO_BOOL = dis.opmap.get("TO_BOOL", 256)
IS_OP = dis.opmap.get("IS_OP", 256)


def frame_op_arg(frame):
    return frame.f_code.co_code[frame.f_lasti + 1]  # TODO: account for EXTENDED_ARG?


class SymbolicSubscriptInterceptor(TracingModule):
    opcodes_wanted = frozenset([BINARY_SUBSCR])

    def trace_op(self, frame, codeobj, codenum):
        # Note that because this is called from inside a Python trace handler, tracing
        # is automatically disabled, so there's no need for a `with NoTracing():` guard.
        key = frame_stack_read(frame, -1)
        if isinstance(key, (int, float, str)):
            return
        # If we got this far, the index is likely symbolic (or perhaps a slice object)
        container = frame_stack_read(frame, -2)
        container_type = type(container)
        if container_type is dict:
            # SimpleDict won't hash the keys it's given!
            wrapped_dict = SimpleDict(list(container.items()))
            frame_stack_write(frame, -2, wrapped_dict)
        elif container_type is list:
            if not isinstance(key, slice):
                # Nothing useful to do with concrete list and symbolic numeric index.
                return
            step = key.step
            if isinstance(step, CrossHairValue) or step not in (None, 1):
                return
            start, stop = key.start, key.stop
            if isinstance(start, SymbolicInt) or isinstance(stop, SymbolicInt):
                view_wrapper = SliceView(container, 0, len(container))
                frame_stack_write(frame, -2, SymbolicList(view_wrapper))


class SymbolicSliceInterceptor(TracingModule):
    opcodes_wanted = frozenset([BINARY_SLICE])

    def trace_op(
        self, frame, codeobj, codenum, _concrete_index_types=(int, float, str)
    ):
        # Note that because this is called from inside a Python trace handler, tracing
        # is automatically disabled, so there's no need for a `with NoTracing():` guard.
        start = frame_stack_read(frame, -1)
        stop = frame_stack_read(frame, -2)
        if isinstance(start, _concrete_index_types) and isinstance(
            stop, _concrete_index_types
        ):
            return
        # If we got this far, the index is likely symbolic (or perhaps a slice object)
        container = frame_stack_read(frame, -3)
        container_type = type(container)
        if container_type is list:
            if isinstance(start, SymbolicInt) or isinstance(stop, SymbolicInt):
                view_wrapper = SliceView(container, 0, len(container))
                frame_stack_write(frame, -3, SymbolicList(view_wrapper))


class DeoptimizedContainer:
    def __init__(self, container):
        self.container = container

    def __contains__(self, other):
        return self.container.__contains__(other)


class SideEffectStashingHashable:
    def __init__(self, fn: Callable):
        self.fn = fn

    def __hash__(self):
        self.result = self.fn()
        return 0


class FormatStashingValue:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        self.formatted = str(self.value)
        return ""

    def __format__(self, fmt: str):
        self.formatted = format(self.value, fmt)
        return ""

    def __repr__(self) -> str:
        self.formatted = repr(self.value)
        return ""


class BoolStashingValue:
    def __init__(self, value, negate):
        self.value = value
        self.negate = negate

    def __bool__(self):
        stashed_bool = self.value.__bool__()
        with NoTracing():
            if self.negate:
                if isinstance(stashed_bool, SymbolicBool):
                    self.stashed_bool = SymbolicBool(z3Not(stashed_bool.var))
                else:
                    self.stashed_bool = not stashed_bool
            else:
                self.stashed_bool = stashed_bool
        return True


_CONTAINMENT_OP_TYPES = tuple(
    i for (i, name) in enumerate(dis.cmp_op) if name in ("in", "not in")
)
assert len(_CONTAINMENT_OP_TYPES) in (0, 2)

_COMPARE_ISOP_TYPES = tuple(
    i for (i, name) in enumerate(dis.cmp_op) if name in ("is", "is not")
)
assert len(_COMPARE_ISOP_TYPES) in (0, 2)


class ComparisonInterceptForwarder(TracingModule):

    opcodes_wanted = frozenset([COMPARE_OP])

    def trace_op(self, frame, codeobj, codenum):
        # Python 3.8 used a general purpose comparison opcode.
        # Forward to dedicated opcode handlers as appropriate.
        compare_type = frame_op_arg(frame)
        if compare_type in _CONTAINMENT_OP_TYPES:
            ContainmentInterceptor.trace_op(None, frame, codeobj, codenum)
        elif compare_type in _COMPARE_ISOP_TYPES:
            IdentityInterceptor.trace_op(None, frame, codeobj, codenum)


class ContainmentInterceptor(TracingModule):

    opcodes_wanted = frozenset([CONTAINS_OP])

    def trace_op(self, frame, codeobj, codenum):
        item = frame_stack_read(frame, -2)
        if not isinstance(item, CrossHairValue):
            return
        container = frame_stack_read(frame, -1)
        containertype = type(container)
        new_container = None
        if containertype is str:
            new_container = DeoptimizedContainer(container)
        elif containertype is set:
            new_container = ShellMutableSet(LinearSet(container))
        elif containertype is dict:
            new_container = SimpleDict(list(container.items()))

        if new_container is not None:
            frame_stack_write(frame, -1, new_container)


class BuildStringInterceptor(TracingModule):
    """
    Adds symbolic handling for the BUILD_STRING opcode (used by f-strings).

    BUILD_STRING concatenates strings from the stack is a fast, but unforgiving way:
    it requires all the substrings to be real Python strings.
    We work around this by replacing the substrings with empty strings, computing the
    concatenation ourselves, and swaping our result in after the opcode completes.
    """

    opcodes_wanted = frozenset([BUILD_STRING])

    def trace_op(self, frame, codeobj, codenum):
        count = frame_op_arg(frame)
        real_result = ""
        for offset in range(-(count), 0):
            substr = frame_stack_read(frame, offset)
            if not isinstance(substr, (str, AnySymbolicStr)):
                raise CrosshairInternal
            # Because we know these are all symbolic or concrete strings, it's ok to
            # not have tracing on when we do the concatenation here:
            real_result += substr
            frame_stack_write(frame, offset, "")

        def post_op():
            frame_stack_write(frame, -1, real_result)

        COMPOSITE_TRACER.set_postop_callback(post_op, frame)


class FormatValueInterceptor(TracingModule):
    """Avoid checks and realization during FORMAT_VALUE (used by f-strings)."""

    opcodes_wanted = frozenset([FORMAT_VALUE, CONVERT_VALUE])

    def trace_op(self, frame, codeobj, codenum):
        flags = frame_op_arg(frame)
        value_idx = -2 if flags == 0x04 else -1
        orig_obj = frame_stack_read(frame, value_idx)

        # FORMAT_VALUE checks that results are concrete strings. So, we format via a
        # a wrapper that returns an empty str, and then swap in the actual string later:

        wrapper = FormatStashingValue(orig_obj)
        if flags in (0x00, 0x01) and isinstance(orig_obj, AnySymbolicStr):
            # Just use the symbolic string directly (don't bother formatting at all)
            wrapper.formatted = orig_obj
            frame_stack_write(frame, value_idx, "")
        else:
            frame_stack_write(frame, value_idx, wrapper)

        def post_op():
            frame_stack_write(frame, -1, wrapper.formatted)

        COMPOSITE_TRACER.set_postop_callback(post_op, frame)


class MapAddInterceptor(TracingModule):
    """De-optimize MAP_ADD over symbolics (used in dict comprehensions)."""

    opcodes_wanted = frozenset([MAP_ADD])

    def trace_op(self, frame: FrameType, codeobj: CodeType, codenum: int) -> None:
        dict_offset = -(frame_op_arg(frame) + 2)
        dict_obj = frame_stack_read(frame, dict_offset)
        if not isinstance(dict_obj, (dict, MutableMapping)):
            raise CrosshairInternal
        # Key and value were swapped in Python 3.8
        key_offset, value_offset = (-2, -1) if version_info >= (3, 8) else (-1, -2)
        key = frame_stack_read(frame, key_offset)
        value = frame_stack_read(frame, value_offset)
        if isinstance(dict_obj, dict):
            if type(key) in ATOMIC_IMMUTABLE_TYPES:
                # Dict and key is (deeply) concrete; continue as normal.
                COMPOSITE_TRACER.set_postop_callback(None, frame)
                return
            else:
                dict_obj = SimpleDict(list(dict_obj.items()))

        # Have the interpreter do a fake assinment.
        # While the fake assignment happens, we'll perform the real assignment secretly
        # when Python hashes the fake key.
        def do_real_assignment():
            dict_obj[key] = value

        frame_stack_write(frame, dict_offset, {})
        frame_stack_write(frame, value_offset, 1)
        frame_stack_write(
            frame, key_offset, SideEffectStashingHashable(do_real_assignment)
        )

        # Afterwards, overwrite the interpreter's resulting dict with ours:
        def post_op():
            frame_stack_write(frame, dict_offset + 2, dict_obj)

        COMPOSITE_TRACER.set_postop_callback(post_op, frame)


class ToBoolInterceptor(TracingModule):
    """Retain symbolic booleans across the TO_BOOL operator."""

    opcodes_wanted = frozenset([TO_BOOL])

    def trace_op(self, frame: FrameType, codeobj: CodeType, codenum: int) -> None:
        input_bool = frame_stack_read(frame, -1)
        if not isinstance(input_bool, CrossHairValue):
            COMPOSITE_TRACER.set_postop_callback(None, frame)
            return
        if isinstance(input_bool, SymbolicBool):
            # TODO: right now, we define __bool__ methods to perform realization.
            # At some point, if that isn't the case, and we can remove this specialized
            # branch for `SybolicBool`.
            frame_stack_write(frame, -1, True)

            def post_op():
                frame_stack_write(frame, -1, input_bool)

        else:
            stashing_value = BoolStashingValue(input_bool, negate=False)
            frame_stack_write(frame, -1, stashing_value)

            def post_op():
                frame_stack_write(frame, -1, stashing_value.stashed_bool)

        COMPOSITE_TRACER.set_postop_callback(post_op, frame)


class NotInterceptor(TracingModule):
    """Retain symbolic booleans across the `not` operator."""

    opcodes_wanted = frozenset([UNARY_NOT])

    def trace_op(self, frame: FrameType, codeobj: CodeType, codenum: int) -> None:
        input_bool = frame_stack_read(frame, -1)
        if not isinstance(input_bool, CrossHairValue):
            COMPOSITE_TRACER.set_postop_callback(None, frame)
            return

        if isinstance(input_bool, SymbolicBool):
            # TODO: right now, we define __bool__ methods to perform realization.
            # At some point, if that isn't the case, and we can remove this specialized
            # branch for `SybolicBool`.
            frame_stack_write(frame, -1, True)

            def post_op():
                frame_stack_write(frame, -1, SymbolicBool(z3Not(input_bool.var)))

        else:
            stashing_value = BoolStashingValue(input_bool, negate=True)
            frame_stack_write(frame, -1, stashing_value)

            def post_op():
                frame_stack_write(frame, -1, stashing_value.stashed_bool)

        COMPOSITE_TRACER.set_postop_callback(post_op, frame)


class SetAddInterceptor(TracingModule):
    """De-optimize SET_ADD over symbolics (used in set comprehensions)."""

    opcodes_wanted = frozenset([SET_ADD])

    def trace_op(self, frame: FrameType, codeobj: CodeType, codenum: int) -> None:
        set_offset = -(frame_op_arg(frame) + 1)
        set_obj = frame_stack_read(frame, set_offset)
        if not isinstance(set_obj, Set):
            raise CrosshairInternal(type(set_obj))
        item = frame_stack_read(frame, -1)
        if isinstance(set_obj, set):
            if isinstance(item, CrossHairValue):
                set_obj = ShellMutableSet(set_obj)
            else:
                # Set and value are concrete; continue as normal.
                COMPOSITE_TRACER.set_postop_callback(None, frame)
                return
        # Have the interpreter do a fake addition, namely `set().add(1)`
        frame_stack_write(frame, set_offset, set())
        frame_stack_write(frame, -1, 1)

        # And do our own addition separately:
        set_obj.add(item)

        # Later, overwrite the interpreter's result with ours:
        def post_op():
            frame_stack_write(frame, set_offset + 1, set_obj)

        COMPOSITE_TRACER.set_postop_callback(post_op, frame)


class IdentityInterceptor(TracingModule):
    """Detect an "is" comparison to symbolics booleans"""

    opcodes_wanted = frozenset([IS_OP])
    # TODO: Adding support for an OptionalSymbolic would now be possible.
    # TODO: it would be amazing to add symbolic enums and support comparison here

    def trace_op(self, frame: FrameType, codeobj: CodeType, codenum: int) -> None:
        arg1 = frame_stack_read(frame, -1)
        arg2 = frame_stack_read(frame, -2)
        if isinstance(arg1, SymbolicBool):
            frame_stack_write(frame, -1, arg1.__ch_realize__())
        if isinstance(arg2, SymbolicBool):
            frame_stack_write(frame, -2, arg2.__ch_realize__())


def make_registrations():
    register_opcode_patch(SymbolicSubscriptInterceptor())
    if sys.version_info >= (3, 12):
        register_opcode_patch(SymbolicSliceInterceptor())
    if sys.version_info < (3, 9):
        register_opcode_patch(ComparisonInterceptForwarder())
    register_opcode_patch(ContainmentInterceptor())
    register_opcode_patch(BuildStringInterceptor())
    register_opcode_patch(FormatValueInterceptor())
    register_opcode_patch(MapAddInterceptor())
    # register_opcode_patch(ToBoolInterceptor())
    register_opcode_patch(NotInterceptor())
    register_opcode_patch(SetAddInterceptor())
    register_opcode_patch(IdentityInterceptor())
