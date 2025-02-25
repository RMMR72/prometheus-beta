def switch_cases(str1: str, str2: str) -> str:
    """
    Take two strings and return a new string with swapped character cases.
    
    If the input strings have different lengths, the returned string will 
    match the length of the shorter input string.
    
    This function follows a specific case-swapping rule:
    - If str2 has a lowercase character, the corresponding str1 character 
      becomes uppercase
    - If str2 has an uppercase character, the corresponding str1 character 
      becomes lowercase
    
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
        # Unique case-swapping rule: 
        # lowercase in str2 -> uppercase in result
        # uppercase in str2 -> lowercase in result
        if str2[i].islower():
            result.append(str1[i].upper())
        else:
            result.append(str1[i].lower())
    
    return ''.join(result)