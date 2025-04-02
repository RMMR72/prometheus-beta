import pytest
import logging
import io
import sys
from unittest.mock import patch
from src.readline_logger import ReadlineLogger

class LogCapture:
    def __init__(self):
        self.log_capture = io.StringIO()
        self.handler = logging.StreamHandler(self.log_capture)
        self.logger = logging.getLogger()
        self.logger.addHandler(self.handler)
        self.logger.setLevel(logging.DEBUG)
    
    def get_log_contents(self):
        return self.log_capture.getvalue()
    
    def cleanup(self):
        self.logger.removeHandler(self.handler)

def test_basic_prompt_logging():
    """Test basic prompt logging functionality."""
    log_capture = LogCapture()
    
    try:
        # Create ReadlineLogger
        readline_logger = ReadlineLogger()
        
        # Simulate user input
        with patch('builtins.input', return_value='test_input'):
            result = readline_logger.log_prompt("Enter something: ")
        
        # Check result and logs
        assert result == 'test_input'
        log_output = log_capture.get_log_contents()
        assert "Prompt: Enter something: " in log_output
        assert "User Input: test_input" in log_output
    finally:
        log_capture.cleanup()

def test_input_validation():
    """Test input validation with a simple validator."""
    # Create a validator that only accepts non-empty strings
    def non_empty_validator(s):
        return bool(s and s.strip())
    
    log_capture = LogCapture()
    
    try:
        # Create ReadlineLogger
        readline_logger = ReadlineLogger()
        
        # First, test valid input
        with patch('builtins.input', return_value='valid input'):
            result = readline_logger.log_prompt("Enter non-empty: ", validator=non_empty_validator)
        assert result == 'valid input'
        
        # Then test invalid input (force empty string)
        with patch('builtins.input', side_effect=['', 'valid input']):
            result = readline_logger.log_prompt("Enter non-empty: ", validator=non_empty_validator)
        assert result == 'valid input'
        
        # Check error logs
        log_output = log_capture.get_log_contents()
        assert "Input validation failed" in log_output
    finally:
        log_capture.cleanup()

def test_custom_log_level():
    """Test custom log level functionality."""
    log_capture = LogCapture()
    
    try:
        # Create ReadlineLogger
        readline_logger = ReadlineLogger()
        
        # Use a custom log level
        with patch('builtins.input', return_value='debug_input'):
            result = readline_logger.log_prompt("Debug prompt: ", log_level=logging.DEBUG)
        
        # Check result and logs
        assert result == 'debug_input'
        log_output = log_capture.get_log_contents()
        assert "Debug prompt: " in log_output
        assert "User Input: debug_input" in log_output
    finally:
        log_capture.cleanup()

def test_error_handling():
    """Test error handling and logging."""
    log_capture = LogCapture()
    
    try:
        # Create ReadlineLogger
        readline_logger = ReadlineLogger()
        
        # Simulate input that raises an exception
        with patch('builtins.input', side_effect=Exception("Simulated input error")):
            with pytest.raises(Exception, match="Simulated input error"):
                readline_logger.log_prompt("Cause an error: ")
        
        # Check error log
        log_output = log_capture.get_log_contents()
        assert "Unexpected error during input" in log_output
    finally:
        log_capture.cleanup()