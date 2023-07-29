import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from bokeh.plotting import figure
import bokeh.plotting as bokeh_plt
from src.economy.product import Product


# TODO: add docstring
class Environment:
    def __init__(self):
        return

    def transform(self):
        return

    def unit(self):
        return


# TODO: add docstring
class Worker:
    def __init__(self, products: list = [], resource_cost: list = []):
        if products and resource_cost:
            if len(products) == len(resource_cost):
                self.products = list()
                for p, v in zip(products, resource_cost):
                    self.products.append([p, v])
            else:
                raise ValueError(f"Number of products and number of resource cost are not the same")
        else:
            self.products = list()
            self.efficiency = list()
        return

    def _init_product(self, products):
        self.products = list()
        for p in products:
            self.products[p.name] = p
        return self.products

    def add_product(self, product, resource_cost):
        self.products.append([product, resource_cost])

    def _dfs(self, nums, target, path, ret):
        if target < 0:
            return
        if target == 0:
            ret.append(path)
            return
        for i in range(len(nums)):
            self._dfs(nums[i:], target - nums[i], path + [nums[i]], ret)

    def _combination(self, candidates, target):
        ret = []
        self._dfs(candidates, target, [], ret)
        return ret

    def max_production(self, resource):
        shape = (len(self.products), len(self.products))
        production = np.zeros(shape)

        for i, p in enumerate(self.products):
            cost = p[1]
            production[i][i] = resource/cost

        return production

    def max_production_combination(self, resource):
        combination_production = []
        candidates = [p[1] for p in self.products]
        com = self._combination(candidates, resource)

        for c in com:
            com_list = []
            for can in candidates:
                count = c.count(can)
                com_list.append(count)
            combination_production.append(com_list)

        return np.array(combination_production)

    def ppf(self, resource):
        ppf_list = []

        for p in self.products:
            t_specilization = resource / p[1]
            ppf_list.append(t_specilization)

        return ppf_list

    def ppf_points(self, time_span):
        points = []

        for p in self.products:
            t_specilization = time_span / p[1]
            point = np.zeros(len(self.products))
            point[self.products.index(p)] = t_specilization
            points.append(point)
        return points


class Supply:
    def __init__(self, price: list, quantity_supplied: list):
        if type(price) != list or type(quantity_supplied) != list:
            raise TypeError(f"price or quantity_supplied parameter should be a list")

        if len(price) != len(quantity_supplied):
            raise ValueError(f"price and quantity_supplied parameter must have the same size")

        self.price = price
        self.quantity_supplied = quantity_supplied

    def __add__(self, other):
        if len(self.price) != len(other.price):
            raise ValueError(f"Size of the two demand class are not the same")

        new_quantity_supplied = []

        for i, v in enumerate(self.quantity_supplied):
            d = v + other.quantity_supplied[i]
            new_quantity_supplied.append(d)

        new_supply = Supply(self.price, list(new_quantity_supplied))

        return new_supply

    def draw(self, show: bool = True, output="mpl"):
        if output == "mpl":
            f = plt.plot(self.quantity_supplied, self.price, color='red')

            if show:
                plt.xlabel("Quantity")
                plt.ylabel("Price")
                plt.show()
            return f
        elif output == "bokeh":
            f = figure(title="Production possibility frontier", x_axis_label="x", y_axis_label="price")
            f.line(self.price, self.quantity_supplied, color='red', line_width=2)

            if show:
                bokeh_plt.show(f)
            return f
        else:
            raise ValueError(f"type parameter should be mpl or bokeh")


class Demand:
    """
    Demand class represent the demand concept in economy
    """
    def __init__(self, price: list, quantity_demanded: list):
        if type(price) != list or type(quantity_demanded) != list:
            raise TypeError(f"price or quantity_demanded parameter should be a list")

        if len(price) != len(quantity_demanded):
            raise ValueError(f"price and quantity_demanded parameter must have the same size")

        self.price = price
        self.quantity_demanded = quantity_demanded

    def __add__(self, other):
        if len(self.price) != len(other.price):
            raise ValueError(f"Size of the two demand class are not the same")

        new_quantity_demanded = []

        for i, v in enumerate(self.quantity_demanded):
            d = v + other.quantity_demanded[i]
            new_quantity_demanded.append(d)

        new_demand = Demand(self.price, list(new_quantity_demanded))

        return new_demand

    def draw(self, show: bool = True, output="mpl"):
        if output == "mpl":
            f = plt.plot(self.quantity_demanded, self.price, color='blue')

            if show:
                plt.xlabel("Quantity")
                plt.ylabel("Price")
                plt.show()
            return f
        elif output == "bokeh":
            f = figure(title="Production possibility frontier", x_axis_label="x", y_axis_label="price")
            f.line(self.price, self.quantity_demanded, color='blue', line_width=2)

            if show:
                bokeh_plt.show(f)
            return f
        else:
            raise ValueError(f"type parameter should be mpl or bokeh")


class Market:
    def __init__(self):
        return

