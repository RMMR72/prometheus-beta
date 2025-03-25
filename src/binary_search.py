def binary_search(arr, target):
    """
    Perform an efficient binary search on a sorted array.
    
    Args:
        arr (list): A sorted list of comparable elements
        target: The element to search for
    
    Returns:
        int: Index of the target element if found, -1 otherwise
    
    Raises:
        TypeError: If input is not a list
        ValueError: If the input list is not sorted
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if the list is sorted
    if not all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
        raise ValueError("Input list must be sorted in ascending order")
    
    # Perform binary search
    left, right = 0, len(arr) - 1
    
    while left <= right:
        # Calculate mid point to avoid potential integer overflow
        mid = left + (right - left) // 2
        
        # Check if target is found
        if arr[mid] == target:
            return mid
        
        # Adjust search boundaries
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    # Target not found
    return -1