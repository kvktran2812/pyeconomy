import numpy as np


# TODO: Check for type of utility
def percentage_reduced_utility_model(utility, percentage):
    """
    Function to apply calculation of utility estimation. The utility drops an amount of percentage from the previous
    value for every 1 unit increase.

    :param utility:
    :param percentage:
    :return:
    """
    if type(utility) is np.ndarray:
        return utility * (percentage/100)
    elif type(utility) is list:
        arr = []
        for i in utility:
            arr.append(i * (percentage/100))
        return arr
    else:
        raise TypeError(f"Utility is not of type list or np.ndarray")


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
    def __init__(self, utils, price):
        self.utils = utils
        self.price = price
        return

    def marginal_util_per_unit(self):
        return

    def calc_marginal_utils(self):
        return

    def convert_to_demand(self):
        return
