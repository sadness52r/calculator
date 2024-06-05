import pytest
from src.calc_methods import summ, sub, mult, div, mod, modulo, summFloat, subFloat, multFloat, divFloat, moduloFloat


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


@pytest.mark.parametrize(
    ('a', 'res'), [
        (2, 2),
        (0, 0),
        (-4, 4),
        (-8, 8),
        (-25, 25),
    ]
)
def test_modulo(a, res):
    assert modulo(a) == res


@pytest.mark.parametrize(
    ('a', 'b', 'res'), [
        (2, 3, 5),
        (3.2, 4.6, 7.8),
        (-4, 6, 2),
        (-8, -8, -16),
        (-25, 25, 0),
        (-0.7, 0.7, 0),
        (-25.3, 25, -0.3),
    ]
)
def test_summFloat(a, b, res):
    assert summFloat(a, b) - res <= 1e-10


@pytest.mark.parametrize(
    ('a', 'b', 'res'), [
        (2, 3, -1),
        (0, 0, 0),
        (-4, 6, -10),
        (-8, -8, 0),
        (-25, 25, -50),
        (-1.2, 0.1, -1.3),
        (6.5, 3.1, 3.4),
        (5.6, 5.6, 0),
    ]
)
def test_subFloat(a, b, res):
    assert subFloat(a, b) - res <= 1e-10


@pytest.mark.parametrize(
    ('a', 'b', 'res'), [
        (2, 3, 6),
        (0, 0, 0),
        (-4, 6, -24),
        (-8, -8, 64),
        (-25, 25, -625),
        (1, 1, 1),
        (1.5, 2, 3),
        (0.1, 2.4, 0.24),
    ]
)
def test_multFloat(a, b, res):
    assert multFloat(a, b) - res <= 1e-10


@pytest.mark.parametrize(
    ('a', 'b', 'res'), [
        (2, 3, 2 / 3),
        (0, 0, 999999999999999999999),
        (0, 5, 0),
        (-4, 6, -4 / 6),
        (-8, -8, 1),
        (-25, 25, -1),
        (1.5, 0.6, 2.5),
    ]
)
def test_divFloat(a, b, res):
    assert divFloat(a, b) - res <= 1e-10


@pytest.mark.parametrize(
    ('a', 'res'), [
        (2, 2),
        (0, 0),
        (-4, 4),
        (-8, 8),
        (-25, 25),
        (-12.3, 12.3),
        (2152.421, 2152.421),
    ]
)
def test_moduloFloat(a, res):
    assert moduloFloat(a) == res
