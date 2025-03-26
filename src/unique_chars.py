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
    
    # Check for non-numeric characters
    if not number_string.isdigit():
        raise ValueError("Input must contain only numeric characters")
    
    # If string is empty, return empty string
    if not number_string:
        return ""
    
    # Manual unique character extraction
    unique_chars = []
    for char in number_string:
        # Only add if character not already in unique_chars
        if char not in unique_chars:
            unique_chars.append(char)
    
    # Convert unique characters back to string
    return ''.join(unique_chars)