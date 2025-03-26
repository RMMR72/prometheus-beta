def remove_duplicates(numbers):
    """
    Remove duplicate values from a list of integers while preserving the original order.
    
    Args:
        numbers (list): A list of integers
    
    Returns:
        list: A new list with duplicates removed, maintaining the original order of first occurrence
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If any element in the list is not an integer
    
    Examples:
        >>> remove_duplicates([1, 2, 3, 2, 4, 1, 5])
        [1, 2, 3, 4, 5]
        >>> remove_duplicates([10, 20, 30, 20, 10, 40, 50])
        [10, 20, 30, 40, 50]
    """
    # Validate input
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Check that all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements must be integers")
    
    # Use a set to track seen numbers while preserving order
    seen = set()
    result = []
    
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    
    return result