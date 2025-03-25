def reverse_integer_array(arr):
    """
    Reverses the order of elements in the given integer array.

    Args:
        arr (list): An input list of integers.

    Returns:
        list: A new list with elements in reverse order.

    Raises:
        TypeError: If the input is not a list.
        TypeError: If the list contains non-integer elements.
    """
    # Validate input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Validate all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    # Return a new list with elements reversed
    return arr[::-1]