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
    
    # Use a set for efficient lookups
    seen = set()
    
    for num in numbers:
        complement = target_sum - num
        
        # Check if the complement exists
        if complement in seen:
            return True
        
        # Add current number to seen
        seen.add(num)
    
    return False