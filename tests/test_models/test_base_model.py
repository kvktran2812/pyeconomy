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
            shift,
            ["data", 5],
            ["data_1"],
            [{"function": shift, "inputs": ["data", 5], "outputs": ["data_1"]}],
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
