def counting_sort(arr):
    """
    Implement the counting sort algorithm for sorting non-negative integers.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: A new sorted list containing the same elements as input.
    
    Raises:
        TypeError: If input is not a list.
        ValueError: If list contains negative numbers.
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list
    if not arr:
        return []
    
    # Find the range of input values
    try:
        max_val = max(arr)
        min_val = min(arr)
    except TypeError:
        raise TypeError("List must contain comparable numeric values")
    
    # Check for negative numbers
    if min_val < 0:
        raise ValueError("Counting sort only works with non-negative integers")
    
    # Create counting array and initialize with zeros
    count = [0] * (max_val + 1)
    
    # Count occurrences of each unique element
    for num in arr:
        count[num] += 1
    
    # Modify count array to store actual position of elements
    sorted_arr = []
    for i, freq in enumerate(count):
        sorted_arr.extend([i] * freq)
    
    return sorted_arr