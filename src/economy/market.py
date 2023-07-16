from typing import List

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from src.economy.product import Product


class Environment:
    def __init__(self):
        return

    def transform(self):
        return

    def unit(self):
        return


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

    # TODO: remove this function
    # def ppf_matrix(self, time_span):
    #     shape = (len(self.products), len(self.products))
    #     matrix = np.zeros(shape)
    #
    #     for p in self.products:
    #         t_specilization = time_span / p[1]
    #         matrix[self.products.index(p)][self.products.index(p)] = t_specilization
    #
    #     return matrix

