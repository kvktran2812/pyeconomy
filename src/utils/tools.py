import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from bokeh.plotting import figure, show


def index(variable):
    """
    function to calculate index number of a variable

    :param variable: the variable to be calculated the index number. Should be a list or iterable object
    :type variable: iterable
    :return: index array
    :rtype: list
    """
    if hasattr(variable, "__iter__"):
        index_arr = []
        initial_value = variable[0]

        for i in variable:
            index_value = (variable[i]/initial_value) * 100
            index_arr.append(index_value)
    else:
        raise TypeError(f"prices parameter is not iterable")
    return index_arr


# TODO: Complete docstring
def draw_supply_demand(supply, demand, output="mpl"):
    """
    Function to draw supply and demand graph

    :param supply:
    :param demand:
    :return:
    """
    if output == "mpl":
        supply.draw(show=False)
        demand.draw(show=False)
        plt.show()
    elif output == "bokeh":
        raise NotImplementedError("Option is not implemented")

    return

