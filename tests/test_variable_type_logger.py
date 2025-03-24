import pytest
import logging
import io
import sys
from src.variable_type_logger import log_variable_type, logger

def test_log_variable_type_primitives():
    """Test logging types of primitive variables."""
    # Redirect the logger's output to a string buffer
    log_capture = io.StringIO()
    handler = logging.StreamHandler(log_capture)
    handler.setFormatter(logging.Formatter('%(message)s'))
    
    # Remove existing handlers and add our new one
    logger.handlers.clear()
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    # Test various primitive types
    assert log_variable_type(42) == "int"
    assert "Variable type: int" in log_capture.getvalue()

    log_capture.truncate(0)
    log_capture.seek(0)
    assert log_variable_type(3.14) == "float"
    assert "Variable type: float" in log_capture.getvalue()

    log_capture.truncate(0)
    log_capture.seek(0)
    assert log_variable_type("hello") == "str"
    assert "Variable type: str" in log_capture.getvalue()

    log_capture.truncate(0)
    log_capture.seek(0)
    assert log_variable_type(True) == "bool"
    assert "Variable type: bool" in log_capture.getvalue()

def test_log_variable_type_containers():
    """Test logging types of container variables."""
    log_capture = io.StringIO()
    handler = logging.StreamHandler(log_capture)
    handler.setFormatter(logging.Formatter('%(message)s'))
    
    logger.handlers.clear()
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    assert log_variable_type([1, 2, 3]) == "list"
    assert "Variable type: list" in log_capture.getvalue()

    log_capture.truncate(0)
    log_capture.seek(0)
    assert log_variable_type((1, 2, 3)) == "tuple"
    assert "Variable type: tuple" in log_capture.getvalue()

    log_capture.truncate(0)
    log_capture.seek(0)
    assert log_variable_type({"a": 1, "b": 2}) == "dict"
    assert "Variable type: dict" in log_capture.getvalue()

def test_log_variable_type_none():
    """Test logging type for None."""
    log_capture = io.StringIO()
    handler = logging.StreamHandler(log_capture)
    handler.setFormatter(logging.Formatter('%(message)s'))
    
    logger.handlers.clear()
    logger.addHandler(handler)
    logger.setLevel(logging.WARNING)

    assert log_variable_type(None) == "NoneType"
    assert "Variable is None" in log_capture.getvalue()

def test_log_variable_type_custom_class():
    """Test logging type for a custom class."""
    class CustomClass:
        pass

    log_capture = io.StringIO()
    handler = logging.StreamHandler(log_capture)
    handler.setFormatter(logging.Formatter('%(message)s'))
    
    logger.handlers.clear()
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    custom_obj = CustomClass()
    assert log_variable_type(custom_obj) == "CustomClass"
    assert "Variable type: CustomClass" in log_capture.getvalue()