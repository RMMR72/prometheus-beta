import pytest
import logging
import io
import sys

from src.error_logger import log_error

class TestErrorLogger:
    def test_error_logging_with_default_message(self, caplog):
        """
        Test that the error logger works with a function that raises an exception
        and logs the default error information.
        """
        @log_error()
        def raise_error():
            raise ValueError("Test error")
        
        # Capture the log
        with caplog.at_level(logging.ERROR):
            with pytest.raises(ValueError):
                raise_error()
        
        # Check log records
        assert len(caplog.records) == 2  # One for error type, one for traceback
        assert "Error in raise_error" in caplog.text
        assert "ValueError" in caplog.text

    def test_error_logging_with_custom_message(self, caplog):
        """
        Test that the error logger works with a custom message.
        """
        @log_error(custom_message="Custom error handling")
        def raise_error():
            raise TypeError("Specific type error")
        
        # Capture the log
        with caplog.at_level(logging.ERROR):
            with pytest.raises(TypeError):
                raise_error()
        
        # Check log records
        assert len(caplog.records) == 2
        assert "Error in raise_error: TypeError - Custom error handling" in caplog.text
        assert "Specific type error" in caplog.text

    def test_error_logging_preserves_function_metadata(self):
        """
        Test that the decorator preserves function metadata.
        """
        @log_error()
        def test_func(x, y):
            """Docstring for test function"""
            return x + y
        
        assert test_func.__name__ == 'test_func'
        assert test_func.__doc__ == 'Docstring for test function'

    def test_error_logging_reraises_exception(self):
        """
        Test that the original exception is re-raised.
        """
        @log_error()
        def raise_error():
            raise RuntimeError("Test runtime error")
        
        with pytest.raises(RuntimeError, match="Test runtime error"):
            raise_error()