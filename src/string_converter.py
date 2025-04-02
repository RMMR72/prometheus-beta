import re

def to_kebab_case(input_string: str) -> str:
    """
    Convert a given string to kebab-case.
    
    Kebab case is a naming convention where words are lowercase and 
    separated by hyphens. This function handles various input formats.
    
    Args:
        input_string (str): The input string to convert to kebab case.
    
    Returns:
        str: The input string converted to kebab case.
    
    Raises:
        TypeError: If input is not a string.
    
    Examples:
        >>> to_kebab_case("Hello World")
        'hello-world'
        >>> to_kebab_case("snake_case_string")
        'snake-case-string'
        >>> to_kebab_case("camelCaseString")
        'camel-case-string'
        >>> to_kebab_case("   Spaced  String   ")
        'spaced-string'
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Strip leading/trailing whitespace
    input_string = input_string.strip()
    
    # Handle empty string
    if not input_string:
        return ""
    
    # Replace multiple consecutive spaces with a single space
    input_string = re.sub(r'\s+', ' ', input_string)
    
    # Replace underscores and spaces with hyphens
    input_string = re.sub(r'[_\s]', '-', input_string)
    
    # Split camelCase and PascalCase
    input_string = re.sub(r'([a-z0-9])([A-Z])', r'\1-\2', input_string)
    
    # Convert to lowercase
    input_string = input_string.lower()
    
    # Remove any non-alphanumeric characters except hyphens
    input_string = re.sub(r'[^a-z0-9-]', '', input_string)
    
    # Remove consecutive hyphens
    input_string = re.sub(r'-+', '-', input_string)
    
    # Remove leading/trailing hyphens
    input_string = input_string.strip('-')
    
    return input_string