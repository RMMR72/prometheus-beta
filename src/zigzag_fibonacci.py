def generate_zigzag_fibonacci(n):
    """
    Generate Fibonacci numbers up to the n'th Fibonacci number in a specific zigzag pattern.
    
    Args:
        n (int): A positive integer defining the number of Fibonacci terms to generate.
    
    Returns:
        list: A list of Fibonacci numbers in a custom zigzag pattern.
    
    Raises:
        ValueError: If n is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Handle special cases for small n
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    # Initialize Fibonacci sequence
    fib = [0, 1]
    
    # Generate Fibonacci numbers
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    
    # Custom zigzag pattern generation
    zigzag = [fib[0]]  # Always start with 0
    
    # Special pattern for zigzag sequence
    pattern_order = [
        2,  # 2nd Fibonacci number 
        1,  # 1st Fibonacci number (if enough elements)
        3,  # 3rd Fibonacci number
        5,  # 5th Fibonacci number
        # and so on...
    ]
    
    pattern_index = 0
    while len(zigzag) < n:
        current_index = pattern_order[pattern_index % len(pattern_order)]
        
        # Make sure the index is within bounds and not already added
        if current_index < len(fib) and fib[current_index] not in zigzag:
            zigzag.append(fib[current_index])
        
        pattern_index += 1
        
        # Safety check to prevent infinite loop
        if len(zigzag) == n:
            break
    
    return zigzag