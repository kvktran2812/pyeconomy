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
        """
        Main function of the model. Loop through each step, run the function and compute the outputs store to data
        variable.

        :return: nothing
        :rtype: None
        """
        for s in self.steps:
            args = self._get_data(s["inputs"])
            f = s["function"]
            outputs = f(*args)
            self._save_data(outputs, s["outputs"])

    def log(self):
        return

    def _save_data(self, outputs, name):
        """
        Helper function to save data to the data variable. This function is used in the step run when the outputs is
        computed.

        :param outputs: outputs to store
        :type outputs: can be any type
        :param name: name to store in the data dict
        :type name: str or iterable
        :return: nothing
        :rtype: None
        """
        if len(name) == 1:
            self.data[name[0]] = outputs
        else:
            for i, v in enumerate(name):
                self.data[v] = outputs[i]

    def _get_data(self, inputs):
        """
        Helper function to get data from data variable. This function is used in the step run when the inputs is
        retrieved before put in functions to compute outputs.

        :param inputs: inputs object to retrieve
        :type inputs: str or iterable
        :return: data that is stored in the data variable
        :rtype: object
        """
        args = []
        for i in inputs:
            if i in self.data:
                args.append(self.data[i])
            else:
                args.append(i)
        return args

    @staticmethod
    def _step_verification(function, inputs, outputs):
        """
        Helper function to verify the step information before add the step to the steps list

        :param function: function to run for this step
        :type function: callable
        :param inputs: inputs for the function to run
        :type inputs: iterable
        :param outputs: outputs to store in the data variable
        :type outputs: str or iterable
        :return: a bool value with a message. True and no error message if step is valid, False and error message
        otherwise.
        :rtype: (bool, str)
        """
        if not callable(function):
            return False, "function parameter is not callable"
        if not hasattr(inputs, "__iter__"):
            return False, "inputs parameter is not iterable"
        if not hasattr(outputs, "__iter__") and type(outputs) is not str:
            return False, "outputs parameter is not iterable or string"
        return True, "No error"

    def add_step(self, function, inputs, outputs):
        """
        Function to add step to this model

        :param function: function to run for this step
        :type function: callable
        :param inputs: inputs for the function to run
        :type inputs: iterable
        :param outputs: outputs to store in the data variable
        :type outputs: str or iterable
        :return: nothing
        :rtype: None
        """
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


