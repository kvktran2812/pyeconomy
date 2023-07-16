import numpy as np
import pandas as pd
import scipy as sp
import math

from src.economy.market import Worker
import matplotlib.pyplot as plt
from bokeh.plotting import figure, show
import itertools as it


# TODO: consider add Environment class to generalize unit value
class PPF:
    def __init__(self, resource=0):
        self.workers = []
        self.resource = resource
        return

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self.workers.append(worker)
        else:
            raise TypeError(f"'worker' parameter must be instance of Worker class")

    def draw(self):
        p = figure(title="Production possibility frontier", x_axis_label="x", y_axis_label="y")

        for w in self.workers:
            ppf_line = w.max_production(self.resource)
            p.line(ppf_line[:, 0], ppf_line[:, 1], line_width=2)
        show(p)

    def max_production_vector(self):
        max_p_vec = []

        for i, w in enumerate(self.workers):
            max_p_vec.append(w.max_production(self.resource))

        return max_p_vec

    def ppf(self):
        w_num = len(self.workers)
        p_num = len(self.workers[0].products)
        w_ppf = [w.ppf(self.resource) for w in self.workers]
        product = it.product(range(p_num), repeat=w_num)
        ppf_arr = []

        for p in product:
            t_arr = [0] * p_num
            for i, v in enumerate(p):
                t_arr[v] += w_ppf[i][v]
            ppf_arr.append(t_arr)
        return ppf_arr

    def most_efficient_ppf(self):
        w_num = len(self.workers)
        p_num = len(self.workers[0].products)
        w_ppf = [w.ppf(self.resource) for w in self.workers]
        product = it.product(range(p_num), repeat=w_num)
        unique = dict()
        ppf_arr = []

        for p in product:
            sorted_p = tuple(sorted(p))
            t_arr = [0] * p_num
            for i, v in enumerate(p):
                t_arr[v] += w_ppf[i][v]

            if sorted_p not in unique:
                unique[sorted_p] = t_arr
            else:
                origin = [0] * p_num
                new_distance = sp.spatial.distance.euclidean(origin, t_arr)
                prev_distance = sp.spatial.distance.euclidean(origin, unique[sorted_p])
                if new_distance > prev_distance:
                    unique[sorted_p] = t_arr
        for i in unique:
            ppf_arr.append(unique[i])
        return ppf_arr

