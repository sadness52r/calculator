import pytest
from src.calc_methods import summ, sub, mult, div, mod


@pytest.mark.parametrize(
    ('a', 'b', 'res'), [
        (2, 3, 5),
        (0, 0, 0),
        (-4, 6, 2),
        (-8, -8, -16),
        (-25, 25, 0),
    ]
)
def test_summ(a, b, res):
    assert summ(a, b) == res


@pytest.mark.parametrize(
    ('a', 'b', 'res'), [
        (2, 3, -1),
        (0, 0, 0),
        (-4, 6, -10),
        (-8, -8, 0),
        (-25, 25, -50),
    ]
)
def test_sub(a, b, res):
    assert sub(a, b) == res


@pytest.mark.parametrize(
    ('a', 'b', 'res'), [
        (2, 3, 6),
        (0, 0, 0),
        (-4, 6, -24),
        (-8, -8, 64),
        (-25, 25, -625),
        (1, 1, 1),
    ]
)
def test_mult(a, b, res):
    assert mult(a, b) == res


@pytest.mark.parametrize(
    ('a', 'b', 'res'), [
        (2, 3, 2 / 3),
        (0, 0, 999999999999999999999),
        (0, 5, 0),
        (-4, 6, -4 / 6),
        (-8, -8, 1),
        (-25, 25, -1),
    ]
)
def test_div(a, b, res):
    assert div(a, b) == res


@pytest.mark.parametrize(
    ('a', 'b', 'res'), [
        (2, 3, 2),
        (0, 0, 999999999999999999998),
        (0, 5, 0),
        (-4, 6, -4 % 6),
        (-8, -8, -8 % -8),
        (-25, 25, -25 % 25),
    ]
)
def test_mod(a, b, res):
    assert mod(a, b) == res
