import json
import logging
import pprint

def log_object(obj, log_level=logging.INFO, logger=None):
    """
    Log an object in a readable, formatted manner.

    Args:
        obj: The object to be logged (can be any type)
        log_level (int, optional): Logging level. Defaults to logging.INFO.
        logger (logging.Logger, optional): Custom logger. 
                If None, uses the root logger.

    Returns:
        str: A formatted string representation of the object

    Raises:
        TypeError: If the object cannot be serialized
    """
    # Use default root logger if no logger is provided
    if logger is None:
        logger = logging.getLogger()

    try:
        # Try JSON serialization first
        try:
            formatted_obj = json.dumps(obj, indent=2)
        except (TypeError, TypeError):
            # If JSON fails, use pretty print
            formatted_obj = pprint.pformat(obj, indent=2)

        # Log the formatted object at the specified log level
        logger.log(log_level, formatted_obj)

        return formatted_obj
    except Exception as e:
        # Handle any unexpected serialization errors
        error_msg = f"Could not log object: {str(e)}"
        logger.error(error_msg)
        raise TypeError(error_msg) from e