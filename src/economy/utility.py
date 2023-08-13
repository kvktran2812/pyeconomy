import numpy as np
from src.utils.functions import percentage_relative_change


# TODO: Check for type of utility
def percentage_reduced_utility_model(utility, percentage, num=0):
    """
    Function to apply calculation of utility estimation. The utility drops an amount of percentage from the previous
    value for every 1 unit increase.

    :param utility:
    :param percentage:
    :param num:
    :return:
    """
    return percentage_relative_change(utility, percentage, num)


def amount_reduced_utility_model(utility, amount):
    if type(utility) is np.ndarray:
        return utility - amount
    elif type(utility) is list:
        arr = []
        for i in utility:
            arr.append(i - amount)
        return arr
    else:
        raise TypeError(f"Utility is not of type list or np.ndarray")
    return


class Utility:
    def __init__(self, units, total_utility, price_per_unit):
        if self._validate_input(total_utility, units, price_per_unit):
            self.total_utility = total_utility
            self.units = units
            self.price_per_unit = price_per_unit
            self.marginal_utility = None
            self.calc_marginal_utils()

    @staticmethod
    def _validate_input(utility, units, price_per_unit):
        if type(utility) is not list and type(utility) is not np.ndarray:
            raise TypeError(f"utility value is not list or np.ndarray")
        if type(units) is not list and type(units) is not np.ndarray:
            raise TypeError(f"units value is not list or np.ndarray")
        if not isinstance(price_per_unit, float) and not isinstance(price_per_unit, int):
            raise TypeError(f"Price must be a number")
        if len(units) != len(utility):
            raise ValueError(f"length of units and utility are not the same")
        return True

    def marginal_util_per_price(self):
        arr = np.zeros(len(self.marginal_utility))
        i = 0
        while i < len(self.marginal_utility):
            arr[i] = self.marginal_utility[i] / self.price_per_unit
            i += 1
        return arr

    def calc_marginal_utils(self):
        self.marginal_utility = np.zeros(len(self.total_utility))
        self.marginal_utility[0] = self.total_utility[0]
        i = 1
        while i < len(self.total_utility):
            self.marginal_utility[i] = self.total_utility[i] - self.total_utility[i-1]
            i += 1

    # TODO: implement this function
    def convert_to_demand(self):
        return
