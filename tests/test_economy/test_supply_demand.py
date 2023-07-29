import pytest
from src.economy.market import Supply, Demand


@pytest.mark.parametrize(
    "price, quantity_supplied",
    [
        (list(range(0, 41, 4)), [0, 0, 0, 0, 0, 1, 3, 5, 7, 9, 11]),
        (list(range(0, 10, 1)), list(range(0, 10, 1))),
    ]
)
def test_supply_init(price, quantity_supplied):
    supply = Supply(price, quantity_supplied)
    assert supply.price == price
    assert supply.quantity_supplied == quantity_supplied


@pytest.mark.parametrize(
    "price, quantity_supplied, error, msg",
    [
        (1, [1, 2, 3, 4], TypeError, "price or quantity_supplied parameter should be a list"),
        ([1, 2, 3], 1, TypeError, "price or quantity_supplied parameter should be a list"),
        ([1, 2, 3, 4], [1, 2, 3], ValueError, "price and quantity_supplied parameter must have the same size"),
        ([1, 2, 3], [1, 2, 3, 4], ValueError, "price and quantity_supplied parameter must have the same size"),
    ]
)
def test_supply_init_error(price, quantity_supplied, error, msg):
    with pytest.raises(error, match=msg):
        supply = Supply(price, quantity_supplied)


@pytest.mark.parametrize(
    "price, quantity_demanded, error, msg",
    [
        (1, [1, 2, 3, 4], TypeError, "price or quantity_demanded parameter should be a list"),
        ([1, 2, 3], 1, TypeError, "price or quantity_demanded parameter should be a list"),
        ([1, 2, 3, 4], [1, 2, 3], ValueError, "price and quantity_demanded parameter must have the same size"),
        ([1, 2, 3], [1, 2, 3, 4], ValueError, "price and quantity_demanded parameter must have the same size"),
    ]
)
def test_demand_init_error(price, quantity_demanded, error, msg):
    with pytest.raises(error, match=msg):
        demand = Demand(price, quantity_demanded)


def test_add_demand():
    price = list(range(10))
    q_demand_1 = list(range(9, -1, -1))
    q_demand_2 = list(range(18, -1, -2))

    demand_1 = Demand(price, q_demand_1)
    demand_2 = Demand(price, q_demand_2)
    demand_3 = demand_1 + demand_2
    arr = []

    for i, v in enumerate(demand_1.quantity_demanded):
        d = v + demand_2.quantity_demanded[i]
        arr.append(d)

    assert arr == demand_3.quantity_demanded
    assert len(demand_3.price) == len(demand_1.price) == len(demand_2.price)

    demand_1.draw(show=False)
    demand_2.draw(show=False)
    demand_3.draw()


def test_add_supply():
    price = list(range(10))
    q_supply_1 = list(range(10))
    q_supply_2 = list(range(0, 20, 2))

    supply_1 = Supply(price, q_supply_1)
    supply_2 = Supply(price, q_supply_2)
    supply_3 = supply_1 + supply_2
    arr = []

    for i, v in enumerate(supply_1.quantity_supplied):
        d = v + supply_2.quantity_supplied[i]
        arr.append(d)

    assert arr == supply_3.quantity_supplied
    assert len(supply_3.price) == len(supply_3.price) == len(supply_3.price)

    supply_1.draw(show=False)
    supply_2.draw(show=False)
    supply_3.draw()


# Visualization
def test_supply_draw():
    prices = list(range(0, 41, 4))
    quantity_supplied = [0, 0, 0, 0, 0, 1, 3, 5, 7, 9, 11]

    supply = Supply(prices, quantity_supplied)
    supply.draw()


def test_demand_draw():
    prices = list(range(0, 41, 4))
    quantity_demanded = list(range(15, 4, -1))

    demand = Demand(prices, quantity_demanded)
    demand.draw()

