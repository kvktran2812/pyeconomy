from src.product import Product
import warnings


class Party:
    def __init__(self, name: str, product_list=None):
        self.name = name
        if not product_list:
            self.products = {}

        # Create storage
        self._storage = {}
        if product_list:
            for product in product_list:
                if not isinstance(product, Product):
                    raise ValueError(f"{product} is not instance of the Product class")
                self._storage[product.name] = 0

    def __str__(self):
        rt_str = f"{self.name}: {self.products}"
        return rt_str

    # -------------------- Property -------------------- #
    @property
    def storage(self):
        return self._storage

    # -------------------- Public functions -------------------- #
    def add_new_product(self, product: Product):
        if self.products and product.name in self.products:
            raise ValueError(f"Product {product.name} has already added in this party, "
                             f"can not add product with similar name, please find another name")
        self.products[product.name] = product
        self._storage[product.name] = 0

    def add_product_to_storage(self, product_name: str, quantity: int = 1):
        if isinstance(product_name, str) and quantity >= 1:
            if product_name not in self._storage:
                self._storage[product_name] = 0
            self._storage[product_name] += quantity

    def party_detail(self):
        print(f"Party: {self.name}")
        print(f"Product: ")
        for key in self.products:
            print(f" - {key}: {self.products[key]}")
        print(f"{self.storage}")

    def sell(self, product, quantity: int = 1, buy_all: bool = True):
        if product not in self.products:
            raise ValueError(f"The party {self.name} doesn't not sell {product}")
        if self._storage[product] - quantity < 0:
            if buy_all:
                quantity = self._storage[product]
                self._storage[product] = 0
                return product, quantity

        self._storage[product] -= quantity
        return product, quantity

    def buy(self, product: str, party, quantity: int = 1):
        if product not in party.products:
            raise ValueError(f"{party.name} party doesn't have {product}")
        if quantity <= 0:
            raise ValueError(f"Quantity should be greater than or equal to 1")

        # add products to storage
        t_product, t_quantity = party.sell(product=product, quantity=quantity)
        self.add_product_to_storage(product_name=t_product, quantity=t_quantity)

    def produce(self, product_name: str, quantity: int = 1):
        # TODO: Correct logic for production
        # TODO: Add a class called Worker to handle the production
        if product_name in self.products:
            self._storage[product_name] += quantity


