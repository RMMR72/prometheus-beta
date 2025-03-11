from typing import List, Union
from collections import Counter

def find_mode(numbers: List[float]) -> Union[float, List[float]]:
    """
    Find the mode(s) of a list of numbers.
    
    Args:
        numbers (List[float]): A list of numbers to find the mode for.
    
    Returns:
        Union[float, List[float]]: 
        - If there's a single mode, returns that number
        - If there are multiple modes, returns a list of those numbers
        - If the input list is empty, returns an empty list
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the list contains non-numeric values
    
    Examples:
        >>> find_mode([1, 2, 2, 3, 4])
        2
        >>> find_mode([1, 2, 2, 3, 3, 4])
        [2, 3]
        >>> find_mode([])
        []
    """
    # Input validation
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list
    if not numbers:
        return []
    
    # Validate numeric values
    try:
        numbers = [float(num) for num in numbers]
    except (TypeError, ValueError):
        raise ValueError("List must contain only numeric values")
    
    # Count occurrences of each number
    count = Counter(numbers)
    
    # Find the maximum frequency
    max_freq = max(count.values())
    
    # Find all numbers with the maximum frequency
    modes = [num for num, freq in count.items() if freq == max_freq]
    
    # Return single mode or list of modes
    return modes[0] if len(modes) == 1 else modes