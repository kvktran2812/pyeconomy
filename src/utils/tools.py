import numpy as np
import scipy as sp


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

