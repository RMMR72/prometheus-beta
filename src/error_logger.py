import logging
import functools
import sys
import traceback

def log_error(custom_message=None):
    """
    A decorator function to log errors with optional custom messages.
    
    Args:
        custom_message (str, optional): A custom message to log with the error. 
                                        Defaults to None.
    
    Returns:
        Decorator that wraps the original function with error logging.
    
    Raises:
        TypeError: If the decorated object is not a callable.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                # Configure logging
                logging.basicConfig(
                    level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s: %(message)s'
                )
                
                # Prepare error details
                error_type = type(e).__name__
                error_details = traceback.format_exc()
                
                # Construct log message
                log_msg = f"Error in {func.__name__}: {error_type}"
                
                # Add custom message if provided
                if custom_message:
                    log_msg += f" - {custom_message}"
                
                # Log the error
                logging.error(log_msg)
                logging.error(error_details)
                
                # Re-raise the exception
                raise
        return wrapper
    return decorator