from src.economy.market import Demand, Supply
from src.utils.functions import *
from src.models.base_model import LinearModel
import matplotlib.pyplot as plt


def func(arg1=1, arg2=2, arg3=3):
    print(arg1, arg2, arg3)


def test_f1(inputs):
    return inputs


model = LinearModel()
model.data["supply"] = [1, 2, 3, 4, 5]
model.add_step(shift, ["supply", 5], ["supply"])
model.add_step(percentage_change, ["supply", 25], ["supply_after_tax"])
model.run()

print(model.data)

plt.plot(model.data["supply"])
plt.plot(model.data["supply_after_tax"])
plt.show()
