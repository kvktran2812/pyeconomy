import numpy as np
import pandas as pd
import scipy as sp

from src.economy.market import Worker
import matplotlib.pyplot as plt
from bokeh.plotting import figure, show

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

    def _production_vector(self):
        first_worker = self.workers[0]
        n_workers = len(self.workers)
        n_products = len(first_worker.products)

        p_vec = np.zeros(shape=(n_workers, n_products))

        for i, w in enumerate(self.workers):
            for j, p in enumerate(w.products):
                p_vec[i, j] = p[1]
        return p_vec

    def ppf(self):
        ppf_arr = []

        for w in self.workers:
            for p in w.products:
                print(p)
            print(w.max_production(self.resource))
        return

