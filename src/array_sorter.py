def sort_array_with_even_squares(arr):
    """
    Sort an array of numbers with a special sorting rule for even numbers.
    
    The function does the following:
    1. Sort the entire array in ascending order
    2. Replace even numbers with their squared values
    
    Args:
        arr (list): A list of numbers to be sorted
    
    Returns:
        list: Sorted array with even numbers replaced by their squared values
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the list contains non-numeric values
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check for non-numeric values
    if not all(isinstance(x, (int, float)) for x in arr):
        raise ValueError("All elements must be numeric")
    
    # Sort the input array
    sorted_arr = sorted(arr)
    
    # Modify the sorted array
    for i in range(len(sorted_arr)):
        if sorted_arr[i] % 2 == 0:
            sorted_arr[i] **= 2
    
    return sorted_arr