import pytest
import logging
import io
import sys
from src.variable_type_logger import log_variable_type

def test_log_variable_type_primitives():
    """Test logging types of primitive variables."""
    # Redirect logging to a string buffer for testing
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO)

    # Test various primitive types
    assert log_variable_type(42) == "int"
    assert "int" in log_capture.getvalue()

    log_capture.truncate(0)
    log_capture.seek(0)
    assert log_variable_type(3.14) == "float"
    assert "float" in log_capture.getvalue()

    log_capture.truncate(0)
    log_capture.seek(0)
    assert log_variable_type("hello") == "str"
    assert "str" in log_capture.getvalue()

    log_capture.truncate(0)
    log_capture.seek(0)
    assert log_variable_type(True) == "bool"
    assert "bool" in log_capture.getvalue()

def test_log_variable_type_containers():
    """Test logging types of container variables."""
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO)

    assert log_variable_type([1, 2, 3]) == "list"
    assert "list" in log_capture.getvalue()

    log_capture.truncate(0)
    log_capture.seek(0)
    assert log_variable_type((1, 2, 3)) == "tuple"
    assert "tuple" in log_capture.getvalue()

    log_capture.truncate(0)
    log_capture.seek(0)
    assert log_variable_type({"a": 1, "b": 2}) == "dict"
    assert "dict" in log_capture.getvalue()

def test_log_variable_type_none():
    """Test logging type for None."""
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.WARNING)

    assert log_variable_type(None) == "NoneType"
    assert "Variable is None" in log_capture.getvalue()

def test_log_variable_type_custom_class():
    """Test logging type for a custom class."""
    class CustomClass:
        pass

    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO)

    custom_obj = CustomClass()
    assert log_variable_type(custom_obj) == "CustomClass"
    assert "CustomClass" in log_capture.getvalue()