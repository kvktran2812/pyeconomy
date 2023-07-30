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
