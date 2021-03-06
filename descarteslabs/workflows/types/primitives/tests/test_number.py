import operator

import pytest

from ...core import ProxyTypeError
from ...containers import Tuple, List
from ..bool_ import Bool
from ..number import Float, Int, Number, _binop_result

from ...core.tests.utils import operator_test


class TestPromote(object):
    def test_number_unpromotable(self):
        with pytest.raises(ProxyTypeError):
            Number._promote(2.2)
        with pytest.raises(ProxyTypeError):
            Number._promote(0)

    def test_primitives(self):
        assert isinstance(Int._promote(0), Int)
        assert isinstance(Float._promote(2.2), Float)

    def test_proxytypes(self):
        assert isinstance(Int._promote(Int(0)), Int)
        assert isinstance(Float._promote(Float(2.2)), Float)

    def test_wrong_primitives(self):
        with pytest.raises(ProxyTypeError):
            Int._promote(2.2)
        with pytest.raises(ProxyTypeError):
            Float._promote(0)

    def test_wrong_proxytypes(self):
        with pytest.raises(
            ProxyTypeError, match=r"You need to convert it explicitly, like `Int\(x\)`"
        ):
            Int._promote(Float(2.2))
        with pytest.raises(
            ProxyTypeError,
            match=r"You need to convert it explicitly, like `Float\(x\)`",
        ):
            Float._promote(Int(0))


class TestConstruct(object):
    def test_explicit_cast_passthrough(self):
        i = Int(Int(1))
        assert i.graft[i.graft["returns"]] == 1

    def test_explicit_cast_to_int(self):
        i = Int(Float(1.0))
        assert isinstance(i, Int)
        assert i.graft[i.graft["returns"]][0] == "Int.cast"

    def test_explicit_cast_to_float(self):
        f = Float(Int(1))
        assert isinstance(f, Float)
        assert f.graft[f.graft["returns"]][0] == "Float.cast"


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (Int(0), Int(0), Int),
        (Float(0.0), Float(0.0), Float),
        (Int(0), Float(0.0), Float),
        (Float(0.0), Int(0), Float),
    ],
)
def test_binop_result(a, b, expected):
    assert _binop_result(a, b) == expected


class TestAllOperators(object):
    int_obj = Int(0)
    float_obj = Float(0.0)
    all_values_to_try = [Int(1), Float(2.2), Bool(True), List[Int]([1, 2])]
    # ^ we use pre-promoted Proxytypes, not py types, since the `operator_test`
    # helper checks if `type(value) is in accepted_types`

    @pytest.mark.parametrize(
        "operator, accepted_types, return_type",
        [
            ["__abs__", (), Int],
            ["__add__", (Int, Float), {Float: Float, Int: Int}],
            ["__div__", (Int, Float), Float],
            [
                "__divmod__",
                (Int, Float),
                {Float: Tuple[Float, Float], Int: Tuple[Int, Int]},
            ],
            ["__eq__", (Int, Float), Bool],
            ["__floordiv__", (Int, Float), {Float: Float, Int: Int}],
            ["__ge__", (Int, Float), Bool],
            ["__gt__", (Int, Float), Bool],
            ["__invert__", (), Int],
            ["__le__", (Int, Float), Bool],
            ["__lt__", (Int, Float), Bool],
            ["__mod__", (Int, Float), {Float: Float, Int: Int}],
            ["__mul__", (Int, Float), {Float: Float, Int: Int}],
            ["__ne__", (Int, Float), Bool],
            ["__neg__", (), Int],
            ["__pos__", (), Int],
            ["__pow__", (Int, Float), {Float: Float, Int: Int}],
            ["__radd__", (Int, Float), {Float: Float, Int: Int}],
            ["__rdiv__", (Int, Float), Float],
            [
                "__rdivmod__",
                (Int, Float),
                {Float: Tuple[Float, Float], Int: Tuple[Int, Int]},
            ],
            ["__rfloordiv__", (Int, Float), {Float: Float, Int: Int}],
            ["__rmod__", (Int, Float), {Float: Float, Int: Int}],
            ["__rmul__", (Int, Float), {Float: Float, Int: Int}],
            ["__rpow__", (Int, Float), {Float: Float, Int: Int}],
            ["__rsub__", (Int, Float), {Float: Float, Int: Int}],
            ["__rtruediv__", (Int, Float), Float],
            ["__sub__", (Int, Float), {Float: Float, Int: Int}],
            ["__truediv__", (Int, Float), Float],
            # Int-specific methods
            ["__and__", [Int], Int],
            ["__lshift__", [Int], Int],
            ["__or__", [Int], Int],
            ["__rand__", [Int], Int],
            ["__rlshift__", [Int], Int],
            ["__ror__", [Int], Int],
            ["__rrshift__", [Int], Int],
            ["__rshift__", [Int], Int],
            ["__rxor__", [Int], Int],
            ["__xor__", [Int], Int],
        ],
    )
    def test_all_operators_int(self, operator, accepted_types, return_type):
        operator_test(
            self.int_obj, self.all_values_to_try, operator, accepted_types, return_type
        )

    @pytest.mark.parametrize(
        "operator, accepted_types, return_type",
        [
            ["__abs__", (), Float],
            ["__add__", (Int, Float), Float],
            ["__div__", (Int, Float), Float],
            ["__divmod__", (Int, Float), Tuple[Float, Float]],
            ["__eq__", (Int, Float), Bool],
            ["__floordiv__", (Int, Float), Float],
            ["__ge__", (Int, Float), Bool],
            ["__gt__", (Int, Float), Bool],
            ["__invert__", (), Float],
            ["__le__", (Int, Float), Bool],
            ["__lt__", (Int, Float), Bool],
            ["__mod__", (Int, Float), Float],
            ["__mul__", (Int, Float), Float],
            ["__ne__", (Int, Float), Bool],
            ["__neg__", (), Float],
            ["__pos__", (), Float],
            ["__pow__", (Int, Float), Float],
            ["__radd__", (Int, Float), Float],
            ["__rdiv__", (Int, Float), Float],
            ["__rdivmod__", (Int, Float), Tuple[Float, Float]],
            ["__rfloordiv__", (Int, Float), Float],
            ["__rmod__", (Int, Float), Float],
            ["__rmul__", (Int, Float), Float],
            ["__rpow__", (Int, Float), Float],
            ["__rsub__", (Int, Float), Float],
            ["__rtruediv__", (Int, Float), Float],
            ["__sub__", (Int, Float), Float],
            ["__truediv__", (Int, Float), Float],
        ],
    )
    def test_all_operators_float(self, operator, accepted_types, return_type):
        operator_test(
            self.float_obj,
            self.all_values_to_try,
            operator,
            accepted_types,
            return_type,
        )

    @pytest.mark.parametrize("obj", [Int(0), Float(2.2)])
    @pytest.mark.parametrize(
        "op, exception",
        [(operator.truth, TypeError), (operator.index, TypeError), (hex, TypeError)],
    )
    def test_unsupported_unary_methods(self, obj, op, exception):
        with pytest.raises(exception):
            op(obj)
