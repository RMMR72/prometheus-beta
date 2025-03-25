def max_subarray_sum(arr):
    """
    Calculate the maximum sum of a contiguous subarray in the given list.
    
    This function uses Kadane's algorithm to find the maximum subarray sum 
    in O(n) time complexity.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        int: The maximum sum of any contiguous subarray
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the list is empty
    
    Examples:
        >>> max_subarray_sum([1, -2, 3, 4, -1, 5])
        11
        >>> max_subarray_sum([-1, -2, -3])
        -1
    """
    # Check for invalid inputs
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if len(arr) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Initialize variables
    max_sum = current_sum = arr[0]
    
    # Iterate through the array using Kadane's algorithm
    for num in arr[1:]:
        # Choose between extending the current subarray or starting a new one
        current_sum = max(num, current_sum + num)
        # Update the maximum sum if current sum is larger
        max_sum = max(max_sum, current_sum)
    
    return max_sum