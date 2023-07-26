from src.economy.product import Product
from src.economy.market import Worker
import matplotlib.pyplot as plt
from src.economy.ppf import PPF
import numpy as np
import itertools as it

from bokeh.plotting import figure, show
from bokeh.layouts import row, column
from scipy.spatial import distance

fish = Product("fish")
apple = Product("apple")

worker0 = Worker()
worker0.add_product(fish, 3)
worker0.add_product(apple, 2)

worker1 = Worker()
worker1.add_product(fish, 2)
worker1.add_product(apple, 4)

worker2 = Worker()
worker2.add_product(fish, 2.4)
worker2.add_product(apple, 2.4)

ppf = PPF(36)
ppf.add_worker(worker0)
ppf.add_worker(worker1)
ppf.add_worker(worker2)

my_ppf = ppf.ppf()
np_ppf = np.array(my_ppf)
np_ppf = np.transpose(np_ppf)

p1 = figure(width=400, height=600)
p1.circle(np_ppf[0], np_ppf[1], size=10, color="navy", alpha=0.5)

my_ppf = ppf.most_efficient_ppf()
np_ppf = np.array(my_ppf)
np_ppf = np.transpose(np_ppf)

p2 = figure(width=400, height=600)
p2.circle(np_ppf[0], np_ppf[1], size=10, color="navy", alpha=0.5)
p2.line(np_ppf[0], np_ppf[1])

show(row([p1, p2]))
