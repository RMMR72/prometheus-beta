def switch_cases(str1: str, str2: str) -> str:
    """
    Take two strings and return a new string with swapped character cases.
    
    If the input strings have different lengths, the returned string will 
    match the length of the shorter input string.
    
    Args:
        str1 (str): First input string (case to be modified)
        str2 (str): Second input string (case source)
    
    Returns:
        str: A new string where characters from str1 are case-swapped using 
             the case of characters from str2
    
    Examples:
        >>> switch_cases("Hello", "world")
        "hELLO"
        >>> switch_cases("PYTHON", "code")
        "code"
    """
    # Handle edge cases
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Both inputs must be strings")
    
    # Determine the length of the shorter string
    min_length = min(len(str1), len(str2))
    
    # Create the result string by swapping cases
    result = []
    for i in range(min_length):
        # If str2's character is uppercase, use lowercase from str1
        # If str2's character is lowercase, use uppercase from str1
        if str2[i].isupper():
            result.append(str1[i].lower())
        else:
            result.append(str1[i].upper())
    
    return ''.join(result)