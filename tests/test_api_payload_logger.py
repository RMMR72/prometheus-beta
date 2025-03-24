import pytest
import logging
import sys
from src.api_payload_logger import log_api_response_payload_size

def test_log_api_response_payload_size_valid_input(caplog):
    # Test with a simple response
    response = {"key": "value"}
    
    # Set log level to INFO
    caplog.set_level(logging.INFO)

    # Call the function
    payload_size = log_api_response_payload_size(response)
    
    # Verify payload size and logging
    assert payload_size > 0
    assert payload_size == sys.getsizeof(response)
    assert f"API Response Payload Size: {payload_size} bytes" in caplog.text

def test_log_api_response_payload_size_invalid_input():
    # Test with non-dictionary input
    with pytest.raises(TypeError, match="Response must be a dictionary"):
        log_api_response_payload_size("not a dict")

    # Test with empty dictionary
    with pytest.raises(ValueError, match="Response cannot be empty"):
        log_api_response_payload_size({})

def test_log_api_response_payload_size_complex_response(caplog):
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
    
    # Set log level to INFO
    caplog.set_level(logging.INFO)

    # Call the function
    payload_size = log_api_response_payload_size(complex_response)
    
    # Verify payload size and logging
    assert payload_size > 0
    assert payload_size == sys.getsizeof(complex_response)
    assert f"API Response Payload Size: {payload_size} bytes" in caplog.text