def find_kth_smallest(arr, k):
    """
    Find the kth smallest element in an array.

    Args:
        arr (list): Input list of comparable elements
        k (int): The k-th smallest element to find (1-based indexing)

    Returns:
        The kth smallest element in the array

    Raises:
        ValueError: If k is less than 1 or greater than the array length, or if list is empty
        TypeError: If input is not a list or k is not an integer
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(k, int):
        raise TypeError("k must be an integer")
    
    # Check for empty list
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Check k is within valid range
    if k < 1 or k > len(arr):
        raise ValueError(f"k must be between 1 and {len(arr)}")
    
    # Sort the array and return the kth smallest element
    # Note: k-1 is used because list indexing is 0-based
    return sorted(arr)[k-1]