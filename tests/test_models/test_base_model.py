from src.economy.market import Demand, Supply
from src.utils.functions import *
from src.models.base_model import LinearModel
import matplotlib.pyplot as plt
import pytest


def test_base_model_init():
    model = LinearModel()
    assert model.data == {}
    assert model.steps == []
    assert not model.verbal


@pytest.mark.parametrize(
    "function, inputs, outputs, results",
    [
        (
            translation,
            ["data", 5],
            ["data_1"],
            [{"function": translation, "inputs": ["data", 5], "outputs": ["data_1"]}],
        ),
        (
            translation,
            ["data", 5],
            "data_1",
            [{"function": translation, "inputs": ["data", 5], "outputs": "data_1"}],
        ),
        (
            percentage_change,
            ["data", 20],
            ["data_1"],
            [
                {
                    "function": percentage_change,
                    "inputs": ["data", 20],
                    "outputs": ["data_1"],
                }
            ],
        ),
    ],
)
def test_model_add_step(function, inputs, outputs, results):
    model = LinearModel()
    model.add_step(function, inputs, outputs)
    assert len(model.steps) == len(results)

    for i, v in enumerate(model.steps):
        f = v["function"]
        inp = v["inputs"]
        out = v["outputs"]
        assert f == results[i]["function"]
        assert inp == results[i]["inputs"]
        assert out == results[i]["outputs"]


@pytest.mark.parametrize(
    "function, inputs, outputs, error_msg",
    [
        (1, ["data"], ["data"], "Error: function parameter is not callable, can not add this step"),
        (translation, 1, ["data"], "Error: inputs parameter is not iterable, can not add this step"),
        (translation, ["data"], 1, "Error: outputs parameter is not iterable or string, can not add this step"),
    ]
)
def test_model_add_step_error(function, inputs, outputs, error_msg):
    model = LinearModel()

    with pytest.raises(ValueError, match=error_msg):
        model.add_step(function, inputs, outputs)
