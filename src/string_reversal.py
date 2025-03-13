def recursive_reverse_string(s: str) -> str:
    """
    Recursively reverse a given string.

    Args:
        s (str): The input string to be reversed.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If input is not a string.
    """
    # Check for invalid input
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Base case: empty string or single character
    if len(s) <= 1:
        return s
    
    # Recursive case: first character moved to end, rest of string recursively reversed
    return recursive_reverse_string(s[1:]) + s[0]