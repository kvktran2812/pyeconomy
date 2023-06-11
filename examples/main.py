from typing import List

from src.economy.product import Product
from src.economy.market import Worker
import matplotlib.pyplot as plt
from src.economy.ppf import PPF
import numpy as np
from bokeh.plotting import figure, show


fish = Product("fish")
apple = Product("apple")

worker0 = Worker()
worker0.add_product(fish, 3)
worker0.add_product(apple, 2)

worker1 = Worker()
worker1.add_product(fish, 2)
worker1.add_product(apple, 4)

ppf = PPF(resource=36)
ppf.add_worker(worker0)
ppf.add_worker(worker1)
ppf.add_worker(worker1)
ppf.add_worker(worker1)

p_vec = ppf._production_vector()
print(p_vec)
