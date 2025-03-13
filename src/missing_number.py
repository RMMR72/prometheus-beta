def find_missing_number(nums):
    """
    Find the missing number in an array of unique positive integers between 1 and n.
    
    Args:
        nums (list): A list of unique positive integers between 1 and n.
    
    Returns:
        int: The missing number in the range.
    
    Raises:
        ValueError: If the input is invalid (empty list, contains duplicates, or out of range).
    """
    # Validate input
    if not nums:
        raise ValueError("Input list cannot be empty")
    
    # Determine the expected range
    n = len(nums) + 1
    
    # Check if all numbers are within the valid range
    if any(num < 1 or num > n for num in nums):
        raise ValueError(f"All numbers must be between 1 and {n}")
    
    # Check for duplicates
    if len(set(nums)) != len(nums):
        raise ValueError("Input must contain unique numbers")
    
    # Use the sum method to find the missing number
    # Sum of numbers from 1 to n: n * (n + 1) // 2
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    
    return expected_sum - actual_sum