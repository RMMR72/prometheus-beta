import logging

# Configure a logger that won't interfere with other loggers
logger = logging.getLogger('variable_type_logger')
logger.setLevel(logging.INFO)

def log_variable_type(variable):
    """
    Log the type of the given variable.

    Args:
        variable: Any Python variable to log the type of.

    Returns:
        str: The type of the variable as a string.

    Raises:
        TypeError: If the variable is None.
    """
    # Ensure the logger has a handler if no handler exists
    if not logger.handlers:
        # Create a StreamHandler
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(levelname)s: %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    # Check for None first to avoid TypeError
    if variable is None:
        logger.warning("Variable is None")
        return "NoneType"
    
    # Get the type of the variable as a string
    var_type = type(variable).__name__
    
    # Log the type with appropriate logging level
    logger.info(f"Variable type: {var_type}")
    
    return var_type