def sum_of_multiples(limit, multiples):
    """
    Calculate the sum of all multiples of given numbers up to a limit.

    Args:
        limit (int): The upper bound (inclusive) for finding multiples.
        multiples (list): A list of integers to find multiples of.

    Returns:
        int: The sum of all unique multiples of the given numbers up to the limit.

    Raises:
        ValueError: If limit or any number in multiples is less than or equal to 0.
    """
    # Validate input
    if limit <= 0:
        raise ValueError("Limit must be a positive integer")
    
    # Validate multiples
    if any(multiple <= 0 for multiple in multiples):
        raise ValueError("All multiples must be positive integers")
    
    if not multiples:
        return 0
    
    # Find all unique numbers divisible by any of the multiples
    unique_multiples = {
        i for i in range(1, limit)
        if any(i % m == 0 for m in multiples if m > 0)
    }
    
    # Return the sum of unique multiples
    return sum(unique_multiples)