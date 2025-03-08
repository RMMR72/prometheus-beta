def count_triangular_numbers(n):
    """
    Count the number of triangular numbers less than or equal to n.
    
    A triangular number is a number that can be represented as a triangular 
    arrangement of points where the first row contains a single element and 
    each subsequent row contains one more element than the previous one.
    
    Triangular numbers follow the formula: T(k) = k * (k + 1) / 2
    
    Args:
        n (int): The upper limit to count triangular numbers.
    
    Returns:
        int: The count of triangular numbers less than or equal to n.
    
    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is negative.
    
    Examples:
        >>> count_triangular_numbers(10)
        4  # 1, 3, 6, 10 are the triangular numbers
        >>> count_triangular_numbers(0)
        0
        >>> count_triangular_numbers(1)
        1
    """
    # Input validation
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # If n is 0, no triangular numbers exist
    if n == 0:
        return 0
    
    # Count triangular numbers
    count = 0
    k = 1
    triangular_num = 1
    
    while triangular_num <= n:
        count += 1
        k += 1
        triangular_num = k * (k + 1) // 2
    
    return count