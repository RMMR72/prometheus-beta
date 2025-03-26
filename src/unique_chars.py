def extract_unique_chars(number_string):
    """
    Extract unique characters from a string of numbers without using built-in unique methods.
    
    Args:
        number_string (str): A string containing numbers.
    
    Returns:
        str: A string with only unique characters, preserving original order.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input contains non-numeric characters.
    """
    # Check input type
    if not isinstance(number_string, str):
        raise TypeError("Input must be a string")
    
    # Empty string is a valid input
    if not number_string:
        return ""
    
    # Check for non-numeric characters
    if not number_string.isdigit():
        raise ValueError("Input must contain only numeric characters")
    
    # Manual unique character extraction that preserves original order
    result = []
    for char in number_string:
        # Only add if character not in result
        if char not in result:
            result.append(char)
    
    # Convert result back to string
    return ''.join(result)