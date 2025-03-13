def has_two_sum(numbers, target_sum):
    """
    Check if there exist two numbers in the array that sum up to the target sum.
    
    Args:
        numbers (list): A list of integers to search through
        target_sum (int): The target sum to find
    
    Returns:
        bool: True if two numbers in the list sum to target_sum, False otherwise
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Examples:
        >>> has_two_sum([1, 2, 3, 4], 7)
        True
        >>> has_two_sum([1, 2, 3, 4], 10)
        False
    """
    # Handle edge cases
    if not numbers or len(numbers) < 2:
        return False
    
    # Use a dictionary to track number frequencies
    num_freq = {}
    
    for num in numbers:
        complement = target_sum - num
        
        # Special handling based on whether target_sum is 0
        if target_sum == 0:
            # For zero sum, need two distinct zero values
            if num == 0:
                if num_freq.get(0, 0) > 0:
                    return True
        else:
            # For non-zero sums
            if complement in num_freq:
                # Ensure we're not using the same number twice
                if complement != num or num_freq[complement] > 1:
                    return True
        
        # Update number frequency
        num_freq[num] = num_freq.get(num, 0) + 1
    
    return False