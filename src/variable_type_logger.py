import logging

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
    # Check for None first to avoid TypeError
    if variable is None:
        logging.warning("Variable is None")
        return "NoneType"
    
    # Get the type of the variable as a string
    var_type = type(variable).__name__
    
    # Log the type with appropriate logging level
    logging.info(f"Variable type: {var_type}")
    
    return var_type