import pytest
from src.economy.market import Party
from src.economy.product import Product


@pytest.mark.parametrize(
    "name, product_list, storage",
    [
        ("Test", [Product(name="fish", prize=1.5, lifetime="1mo")], 1),
        ("Test", [], 0)
    ]
)
def test_party_initialization(name, product_list, storage):
    test_party = Party(name=name, product_list=product_list)

    assert test_party.name == "Test"
    assert len(test_party.storage) == storage


def test_party_initialization_error():
    with pytest.raises(ValueError):
        test_party = Party(name="Test", product_list=[0, 1, 2])


@pytest.mark.parametrize(
    "product, quantity, result",
    [
        ("fish", 30, 30),
        ("fish", 120, 100)
    ]
)
def test_party_get_and_sell(product, quantity, result):
    party1 = Party(name="A")
    party2 = Party(name="B")

    party1.add_new_product(product=Product(name="fish", prize=1.5, lifetime="1mo"))
    party1.storage["fish"] = 100

    party2.buy(product=product, party=party1, quantity=quantity)

    assert party2.storage["fish"] == result

