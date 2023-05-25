from src.market import Party
from src.product import Product


if __name__ == "__main__":
    party1 = Party(name="A")
    party2 = Party(name="B")

    party1.add_new_product(product=Product(name="fish", prize=1.5, lifetime="1mo"))
    party1.add_new_product(product=Product(name="shrimp", prize=1.5, lifetime="1mo"))
    party1.add_new_product(product=Product(name="crab", prize=1.5, lifetime="1mo"))

    party1.party_detail()
