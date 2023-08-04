import abc
from abc import ABC
import networkx as nx
import logging


class LinearModel:
    def __init__(self):
        self.data = {}
        self.steps = []

    def run(self):
        for s in self.steps:
            args = self.get_data(s["inputs"])
            f = s["function"]
            output = f(*args)

            if len(s["outputs"]) == 1:
                self.data[s["outputs"][0]] = output
            else:
                for i, v in enumerate(s["outputs"]):
                    self.data[v] = output[i]

    def log(self):
        return

    def _save_data(self):

        return

    def _get_data(self, inputs):
        args = []
        for i in inputs:
            if i in self.data:
                args.append(self.data[i])
            else:
                args.append(i)
        return args

    def add_step(self, function, inputs, outputs):
        step = {
            "function": function,
            "inputs": inputs,
            "outputs": outputs,
        }
        self.steps.append(step)

