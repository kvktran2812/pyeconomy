import pytest
from src.economy.market import Supply, Demand


# @pytest.mark.parametrize
def test_supply_init():
    prices = list(range(0, 41, 4))
    quantity_supplied = [0, 0, 0, 0, 0, 1, 3, 5, 7, 9, 11]

    assert len(prices) == len(quantity_supplied)
    supply = Supply(prices, quantity_supplied)
    assert supply.price == prices
    assert supply.quantity_supplied == quantity_supplied



