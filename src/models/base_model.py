import abc
from abc import ABC
import networkx as nx
import logging


# TODO: Add docstring
class LinearModel:
    """
    A linear model class is used to represent computing of economic model. The computation is base on the steps of the
    model, linearly from inputs step by step to outputs.
    """
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

    @staticmethod
    def _step_verification(function, inputs, outputs):
        if not callable(function):
            return False, "function parameter is not callable"
        if not hasattr(inputs, "__iter__"):
            return False, "inputs parameter is not iterable"
        if not hasattr(outputs, "__iter__") and type(outputs) is not str:
            return False, "outputs parameter is not iterable or string"
        return True, "No error"

    def add_step(self, function, inputs, outputs):
        status, msg = self._step_verification(function, inputs, outputs)
        if status:
            step = {
                "function": function,
                "inputs": inputs,
                "outputs": outputs,
            }
            self.steps.append(step)
        else:
            raise ValueError(f"Error: {msg}, can not add this step")


