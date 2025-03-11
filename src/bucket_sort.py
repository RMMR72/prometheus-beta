def bucket_sort(arr, num_buckets=None):
    """
    Implements the bucket sort algorithm for sorting a list of numbers.
    
    Args:
        arr (list): The input list of numbers to be sorted.
        num_buckets (int, optional): Number of buckets to use. 
                                     Defaults to None (automatically determined).
    
    Returns:
        list: A new sorted list.
    
    Raises:
        TypeError: If input is not a list or contains non-numeric elements.
        ValueError: If input list is empty.
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if len(arr) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Check if all elements are numeric
    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("All elements must be numeric")
    
    # If no bucket number specified, use square root of list length
    if num_buckets is None:
        num_buckets = max(int(len(arr) ** 0.5), 1)
    
    # Find min and max to determine bucket range
    if len(arr) <= 1:
        return arr.copy()
    
    min_val = min(arr)
    max_val = max(arr)
    
    # Handle case where all elements are the same
    if min_val == max_val:
        return arr.copy()
    
    # Create buckets
    buckets = [[] for _ in range(num_buckets)]
    
    # Distribute elements into buckets
    value_range = max_val - min_val
    for num in arr:
        # Calculate bucket index
        bucket_index = min(num_buckets - 1, int(((num - min_val) / value_range) * (num_buckets - 1)))
        buckets[bucket_index].append(num)
    
    # Sort individual buckets
    sorted_buckets = []
    for bucket in buckets:
        # Use built-in sort for each bucket
        sorted_buckets.extend(sorted(bucket))
    
    return sorted_buckets