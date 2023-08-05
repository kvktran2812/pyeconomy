import abc
from abc import ABC
import networkx as nx
import logging


class LinearModel:
    def __init__(self):
        self.data = {}
        self.steps = []
        self.verbal = False

    def run(self):
        for s in self.steps:
            args = self._get_data(s["inputs"])
            f = s["function"]
            outputs = f(*args)
            self._save_data(outputs, s["outputs"])

    def log(self):
        return

    def _save_data(self, outputs, name):
        if len(name) == 1:
            self.data[name[0]] = outputs
        else:
            for i, v in enumerate(name):
                self.data[v] = outputs[i]

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

