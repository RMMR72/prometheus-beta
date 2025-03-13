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
        
        # Check if the complement exists and has enough frequency
        if complement in num_freq:
            # For non-zero sums, ensure we're not using the same number twice
            # For zero sums, ensure we have at least two instances of the number
            if complement != num or num_freq[complement] > 1:
                return True
        
        # Update number frequency
        num_freq[num] = num_freq.get(num, 0) + 1
    
    return False