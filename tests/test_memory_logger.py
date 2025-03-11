import pytest
import logging
import psutil
from src.memory_logger import log_memory_usage

class MockLogger:
    def __init__(self):
        self.logged_messages = []
    
    def info(self, message):
        self.logged_messages.append(('info', message))
    
    def error(self, message):
        self.logged_messages.append(('error', message))

def test_log_memory_usage():
    """Test that memory usage logging works correctly"""
    mock_logger = MockLogger()
    
    # Call the function
    result = log_memory_usage(mock_logger)
    
    # Verify the result structure
    assert isinstance(result, dict)
    assert 'total_memory' in result
    assert 'available_memory' in result
    assert 'used_memory' in result
    assert 'memory_percent' in result
    
    # Check logging occurred
    assert len(mock_logger.logged_messages) > 0
    assert mock_logger.logged_messages[0][0] == 'info'

def test_memory_usage_values():
    """Test that memory usage values are reasonable"""
    result = log_memory_usage()
    
    # Total memory should be positive
    assert result['total_memory'] > 0
    
    # Memory percentages should be between 0 and 100
    assert 0 <= result['memory_percent'] <= 100
    
    # Used memory should not exceed total memory
    assert result['used_memory'] <= result['total_memory']

def test_default_logger():
    """Test that the function works with default logger"""
    # This test ensures no exception is raised when no logger is provided
    result = log_memory_usage()
    assert result is not None

def test_error_handling():
    """Ensure errors are logged and raised"""
    # We'll simulate this by using a tracking mechanism
    class BrokenMemory:
        def __init__(self):
            self.total = None
    
    # Mock psutil to raise an exception
    original_virtual_memory = psutil.virtual_memory
    psutil.virtual_memory = lambda: BrokenMemory()
    
    with pytest.raises(Exception):
        log_memory_usage()
    
    # Restore the original function
    psutil.virtual_memory = original_virtual_memory