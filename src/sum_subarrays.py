def sum_subarrays(arr, k):
    """
    Calculate the sum of all elements in subarrays with length less than or equal to k.

    Args:
        arr (list): A sorted list of integers.
        k (int): Maximum subarray length to consider.

    Returns:
        int: Sum of all elements in subarrays of length <= k.

    Raises:
        TypeError: If arr is not a list or k is not an integer.
        ValueError: If k is negative.
    """
    # Type checking
    if not isinstance(arr, list):
        raise TypeError("Input 'arr' must be a list")
    if not isinstance(k, int):
        raise TypeError("Input 'k' must be an integer")
    
    # Value validation
    if k < 0:
        raise ValueError("Input 'k' must be non-negative")
    
    # If k is 0 or arr is empty, return 0
    if k == 0 or not arr:
        return 0
    
    # Initialize total sum
    total_sum = 0
    
    # Iterate through all possible start indices
    for start in range(len(arr)):
        # Current subarray accumulator
        curr_subarray = []
        
        # Iterate through possible end indices
        for end in range(start, len(arr)):
            # Add the current element to the subarray
            curr_subarray.append(arr[end])
            
            # If current subarray length exceeds k, stop
            if len(curr_subarray) > k:
                break
            
            # Sum the current subarray and add to total
            total_sum += sum(curr_subarray)
    
    return total_sum