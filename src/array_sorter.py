def sort_array_with_even_squares(arr):
    """
    Sort an array of numbers with a special sorting rule for even numbers.
    
    The function does the following:
    1. Sort the entire array in ascending order
    2. Square the even numbers
    3. Sort the even number squares in descending order
    4. Replace the original even numbers with their sorted squared values
    
    Args:
        arr (list): A list of numbers to be sorted
    
    Returns:
        list: Sorted array with even number squares sorted in descending order
    
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
    
    # Create a copy of the original array to avoid modifying the input
    sorted_arr = sorted(arr)
    
    # Identify indices of even numbers
    even_indices = [i for i in range(len(sorted_arr)) if sorted_arr[i] % 2 == 0]
    
    # Square the even numbers
    even_squares = [sorted_arr[i]**2 for i in even_indices]
    
    # Sort even squares in descending order
    descending_squares = sorted(even_squares, reverse=True)
    
    # Replace even numbers with their sorted squared values
    for i, idx in enumerate(even_indices):
        sorted_arr[idx] = descending_squares[i]
    
    return sorted_arr