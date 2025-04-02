import re

def to_dot_case(input_string):
    """
    Convert a given string to dot case.
    
    Dot case is a string formatting style where words are separated by dots,
    and all characters are lowercase.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The input string converted to dot case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> to_dot_case("HelloWorld")
        'hello.world'
        >>> to_dot_case("hello_world")
        'hello.world'
        >>> to_dot_case("Hello World")
        'hello.world'
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Remove leading/trailing whitespace
    input_string = input_string.strip()
    
    # If empty string, return empty string
    if not input_string:
        return ""
    
    # First, replace any underscores or hyphens with spaces
    input_string = re.sub(r'[_-]', ' ', input_string)
    
    # Split camelCase or PascalCase
    input_string = re.sub(r'(?<!^)(?=[A-Z])', ' ', input_string)
    
    # Split by spaces, convert to lowercase, and join with dot
    return '.'.join(word.lower() for word in input_string.split())