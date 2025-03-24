import logging
import sys
from typing import Any, Dict, Optional

def log_api_response_payload_size(response: Dict[str, Any], 
                                   logger: Optional[logging.Logger] = None) -> int:
    """
    Log the size of an API response payload.

    Args:
        response (Dict[str, Any]): The API response dictionary.
        logger (Optional[logging.Logger]): Optional custom logger. 
                                           If not provided, uses root logger.

    Returns:
        int: Size of the payload in bytes.

    Raises:
        TypeError: If response is not a dictionary.
        ValueError: If response is empty.
    """
    # Validate input
    if not isinstance(response, dict):
        raise TypeError("Response must be a dictionary")
    
    if not response:
        raise ValueError("Response cannot be empty")

    # Use provided logger or root logger
    log = logger or logging.getLogger()

    # Calculate payload size
    try:
        payload_size = sys.getsizeof(response)
        
        # Log the payload size
        log.info(f"API Response Payload Size: {payload_size} bytes")
        
        return payload_size
    except Exception as e:
        log.error(f"Error calculating payload size: {e}")
        raise