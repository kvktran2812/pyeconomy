import math
import numpy as np


def non_linear_curve(series, a, b, c, round_number=2):
    """
    Non-linear curve function to create a curve y(x). It is used to create non-linear demand supply curve.
    Formula: y(x) = (a/x +c)*b

    :param series:
    :param a:
    :param b:
    :param c:
    :param round_number:
    :return:
    """
    curve = []
    for x in series:
        if x == 0:
            curve.append(np.Inf)
            continue
        y = (a/x + c)*b
        curve.append(round(y, round_number))
    return curve


def linear_curve(series, a, b, round_number=2):
    """
    Function to create linear function y(x) = ax + b

    :param series:
    :param a:
    :param b:
    :param round_number:
    :return:
    """
    line = []
    for x in series:
        y = a*x + b
        line.append(round(y, round_number))
    return line


def logarithm_curve(series, base, round_number=2):
    """
    Logarithm function

    :param series:
    :param base:
    :param round_number:
    :return:
    """
    curve = []
    for x in series:
        y = math.log(x, base)
        curve.append(round(y, 2))
    return curve


# TODO: Check usefulness of this function
def translation(series, value=0):
    """
    Increase or decrease all of the series member value by the value provided

    :param series:
    :param value:
    :return:
    """
    if type(series) is not list and type(series) is not np.ndarray:
        raise TypeError("Type of series is not list or np.ndarray")
    if value == 0:
        return series
    return [x+value for x in series]


# TODO: Check usefulness of this function
def percentage_change(series, percentage=0):
    """
    Increase or decrease all of the series member value by a percentage provided

    :param series:
    :param percentage:
    :return:
    """
    if percentage == 0:
        return series
    return [x+(x*percentage/100) for x in series]
