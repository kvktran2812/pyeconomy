import pytest
import numpy as np


@pytest.mark.parametrize(
    "val1, val2, error, msg",
    [
        (1, [1, 2, 3], TypeError, "The type of the two value provided must be a list"),
        ([1, 2, 3], 1, TypeError, "The type of the two value provided must be a list"),
        ([1, 2], [1, 2, 3], ValueError, "Size of the two value are not the same")
    ]
)
def test_elasticity_error(val1, val2, error, msg):
    with pytest.raises(error, match=msg):
        percentage_change_elasticity(val1, val2)


def test_elasticity_result():
    demand = list(range(0, 11, 1))
    price = list(range(10, -1, -1))

    e = percentage_change_elasticity(demand, price)
    assert e == [np.Inf, -9.0, -4.0, -2.3333333333333335, -1.5, -1.0, -0.6666666666666666, -0.42857142857142855, -0.25, -0.1111111111111111]
    assert len(demand) == len(price)
