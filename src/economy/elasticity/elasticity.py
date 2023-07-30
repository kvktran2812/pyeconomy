from src.economy.market import Demand, Supply


def percentage_change_elasticity(p_change_val1, p_change_val2):
    """
    
    :param p_change_val1:
    :param p_change_val2:
    :return:
    """
    if not len(p_change_val2) == len(p_change_val1):
        raise ValueError("Size of the two value are not the same")

    elasticity = []

    for i, v in enumerate(p_change_val1):
        if i == 0:
            continue
        if p_change_val1[i - 1] == 0 or p_change_val2[i - 1] == 0:
            elasticity.append("NaN")
            continue
        p_change_1 = (p_change_val1[i] - p_change_val1[i - 1]) / p_change_val1[i - 1]
        p_change_2 = (p_change_val2[i] - p_change_val2[i - 1]) / p_change_val2[i - 1]
        e_val = p_change_1 / p_change_2
        elasticity.append(e_val)

    return elasticity

