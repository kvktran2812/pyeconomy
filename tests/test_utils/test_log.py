import pytest
from src.utils.log import *
import os
from pathlib import Path


def test_custom_formatter():
    assert CustomFormatter.grey == "\x1b[37m"
    assert CustomFormatter.yellow == "\x1b[33;20m"
    assert CustomFormatter.red == "\x1b[31;20m"
    assert CustomFormatter.bold_red == "\x1b[31;1m"
    assert CustomFormatter.reset == "\x1b[0m"


# TODO: clear and remove log file or make it log somewhere else
@pytest.mark.parametrize(
    "name, file_handler, no_handler",
    [
        ("MyModel", False, 1),
        ("MyModel", True, 2),
    ],
)
def test_model_logger(name, file_handler, no_handler):
    logger = ModelLogger(name=name, log_to_file=file_handler)
    assert logger.name == name
    assert len(logger.handlers) == no_handler
