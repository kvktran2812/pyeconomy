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

