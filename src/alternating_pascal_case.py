def convert_to_alternating_pascal_case(input_string: str) -> str:
    """
    Convert a given string to alternating Pascal case.
    
    Rules:
    - Remove any non-alphanumeric characters
    - Split the string into words
    - Capitalize words at even indices 
    - Lowercase words at odd indices
    
    Args:
        input_string (str): The input string to convert
    
    Returns:
        str: The string converted to alternating Pascal case
    
    Raises:
        TypeError: If input is not a string
    
    Examples:
        >>> convert_to_alternating_pascal_case("hello world")
        'HelloWorld'
        >>> convert_to_alternating_pascal_case("PYTHON is AWESOME")
        'PythonIsAwesome'
        >>> convert_to_alternating_pascal_case("123 test case!")
        'TestCase'
    """
    # Validate input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Remove non-alphanumeric characters and split into words
    import re
    words = re.findall(r'\w+', input_string)
    
    # Handle empty input
    if not words:
        return ''
    
    # Convert words to alternating case
    converted_words = [
        word.capitalize() if i % 2 == 0 else word.lower() 
        for i, word in enumerate(words)
    ]
    
    # Join the words
    return ''.join(converted_words)