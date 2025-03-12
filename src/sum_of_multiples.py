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
    
    if not multiples:
        return 0
    
    for multiple in multiples:
        if multiple <= 0:
            raise ValueError("All multiples must be positive integers")
    
    # Use a set to store unique multiples to avoid double-counting
    unique_multiples = set()
    
    # Find all multiples for each number in the multiples list
    for multiple in multiples:
        # Generate multiples of the current number up to the limit
        current_multiples = range(multiple, limit + 1, multiple)
        unique_multiples.update(filter(lambda x: x <= limit, current_multiples))
    
    # Return the sum of unique multiples
    return sum(unique_multiples)