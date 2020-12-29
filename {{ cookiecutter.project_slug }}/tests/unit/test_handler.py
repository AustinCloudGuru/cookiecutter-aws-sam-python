import json
import pytest
from {{ cookiecutter.function_name }} import handler

def test_handler(mocker):
    ret = handler.lambda_handler({}, None)
    assert ret == "It works!"
