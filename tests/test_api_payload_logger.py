import pytest
import logging
import sys
from src.api_payload_logger import log_api_response_payload_size

def test_log_api_response_payload_size_valid_input():
    # Test with a simple response
    response = {"key": "value"}
    
    # Create a mock logger to capture logs
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)
    
    # Capture logs
    log_capture = []
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(message)s')
    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)
    
    def log_capture_handler(record):
        log_capture.append(record.getMessage())
    
    logger.addHandler(handler)
    logger.info = log_capture_handler

    # Call the function
    payload_size = log_api_response_payload_size(response, logger)
    
    # Verify payload size
    assert payload_size > 0
    assert payload_size == sys.getsizeof(response)
    assert f"API Response Payload Size: {payload_size} bytes" in log_capture[0]

def test_log_api_response_payload_size_invalid_input():
    # Test with non-dictionary input
    with pytest.raises(TypeError, match="Response must be a dictionary"):
        log_api_response_payload_size("not a dict")

    # Test with empty dictionary
    with pytest.raises(ValueError, match="Response cannot be empty"):
        log_api_response_payload_size({})

def test_log_api_response_payload_size_complex_response():
    # Test with a more complex response
    complex_response = {
        "user": {
            "id": 123,
            "name": "John Doe",
            "email": "john@example.com"
        },
        "items": [1, 2, 3, 4, 5],
        "metadata": {
            "created_at": "2023-01-01",
            "updated_at": "2023-02-01"
        }
    }
    
    # Create a mock logger
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)
    
    # Call the function
    payload_size = log_api_response_payload_size(complex_response, logger)
    
    # Verify payload size
    assert payload_size > 0
    assert payload_size == sys.getsizeof(complex_response)