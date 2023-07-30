import pytest
from src.utils.functions import *


@pytest.mark.parametrize(
    "series, a, b, c, result",
    [
        (
            list(range(15, 2, -1)),
            10,
            10,
            10,
            [
                106.67,
                107.14,
                107.69,
                108.33,
                109.09,
                110.0,
                111.11,
                112.5,
                114.29,
                116.67,
                120.0,
                125.0,
                133.33,
            ],
        ),
        (
            list(range(10, 2, -1)),
            10,
            5,
            2,
            [15.0, 15.56, 16.25, 17.14, 18.33, 20.0, 22.5, 26.67],
        ),
    ],
)
def test_linear_curve_function(series, a, b, c, result):
    value = non_linear_curve(series, a, b, c)
    assert value == result


@pytest.mark.parametrize(
    "series, a, b,  result",
    [
        (list(range(10, 2, -1)), 10, 2, [102, 92, 82, 72, 62, 52, 42, 32]),
        (list(range(10, 2, -1)), -5, 2, [-48, -43, -38, -33, -28, -23, -18, -13]),
    ],
)
def test_non_linear_function(series, a, b, result):
    value = linear_curve(series, a, b)
    assert value == result


@pytest.mark.parametrize(
    "series, base, result",
    [
        (
            list(range(1, 100, 5)),
            2,
            [
                0.0,
                2.58,
                3.46,
                4.0,
                4.39,
                4.7,
                4.95,
                5.17,
                5.36,
                5.52,
                5.67,
                5.81,
                5.93,
                6.04,
                6.15,
                6.25,
                6.34,
                6.43,
                6.51,
                6.58,
            ],
        ),
        (
            list(range(1, 100, 5)),
            5,
            [
                0.0,
                1.11,
                1.49,
                1.72,
                1.89,
                2.02,
                2.13,
                2.23,
                2.31,
                2.38,
                2.44,
                2.5,
                2.55,
                2.6,
                2.65,
                2.69,
                2.73,
                2.77,
                2.8,
                2.84,
            ],
        ),
    ],
)
def test_logarithm_curve(series, base, result):
    value = logarithm_curve(series, base)
    assert value == result
