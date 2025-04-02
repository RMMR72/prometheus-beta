import pytest
import logging
import io
import sys
from unittest.mock import patch
from src.readline_logger import ReadlineLogger

def test_basic_prompt_logging():
    """Test basic prompt logging functionality."""
    # Capture logs
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO)
    logger = logging.getLogger()
    
    # Create ReadlineLogger
    readline_logger = ReadlineLogger(logger)
    
    # Simulate user input
    with patch('builtins.input', return_value='test_input'):
        result = readline_logger.log_prompt("Enter something: ")
    
    # Check result and logs
    assert result == 'test_input'
    log_output = log_capture.getvalue()
    assert "Prompt: Enter something: " in log_output
    assert "User Input: test_input" in log_output

def test_input_validation():
    """Test input validation with a simple validator."""
    # Create a validator that only accepts non-empty strings
    def non_empty_validator(s):
        return bool(s and s.strip())
    
    # Capture logs and errors
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.ERROR)
    logger = logging.getLogger()
    
    # Create ReadlineLogger
    readline_logger = ReadlineLogger(logger)
    
    # First, test valid input
    with patch('builtins.input', return_value='valid input'):
        result = readline_logger.log_prompt("Enter non-empty: ", validator=non_empty_validator)
    assert result == 'valid input'
    
    # Then test invalid input (force empty string)
    with patch('builtins.input', side_effect=['', 'valid input']):
        result = readline_logger.log_prompt("Enter non-empty: ", validator=non_empty_validator)
    assert result == 'valid input'
    
    # Check error logs
    log_output = log_capture.getvalue()
    assert "Input validation error" in log_output

def test_custom_log_level():
    """Test custom log level functionality."""
    # Capture logs
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.DEBUG)
    logger = logging.getLogger()
    
    # Create ReadlineLogger
    readline_logger = ReadlineLogger(logger)
    
    # Use a custom log level
    with patch('builtins.input', return_value='debug_input'):
        result = readline_logger.log_prompt("Debug prompt: ", log_level=logging.DEBUG)
    
    # Check result and logs
    assert result == 'debug_input'
    log_output = log_capture.getvalue()
    assert "Debug prompt: " in log_output
    assert "User Input: debug_input" in log_output

def test_error_handling():
    """Test error handling and logging."""
    # Prepare logging
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.ERROR)
    logger = logging.getLogger()
    
    # Create ReadlineLogger
    readline_logger = ReadlineLogger(logger)
    
    # Simulate input that raises an exception
    with patch('builtins.input', side_effect=Exception("Simulated input error")):
        with pytest.raises(Exception, match="Simulated input error"):
            readline_logger.log_prompt("Cause an error: ")
    
    # Check error log
    log_output = log_capture.getvalue()
    assert "Unexpected error during input" in log_output