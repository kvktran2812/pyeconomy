import pytest
import datetime
from src.economy.product import Product


def test_product_init_0():
    t_product = Product(name="fish")

    assert t_product.name == "fish"
    assert t_product.prize == 0.0
    assert t_product.lifetime == ""
    assert t_product.materials == {}
    assert t_product.mfg_date == datetime.date.today()
    assert t_product.exp_date == datetime.date.today()


def test_product_init_1():
    pass


def test_product_str():
    t_product = Product(name="Fish")
    assert t_product.__str__() == f"{t_product.lifetime} {t_product.materials}"

