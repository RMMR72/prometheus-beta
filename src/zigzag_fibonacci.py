def generate_zigzag_fibonacci(n):
    """
    Generate Fibonacci numbers up to the n'th Fibonacci number in a zigzag pattern.
    
    Args:
        n (int): A positive integer defining the number of Fibonacci terms to generate.
    
    Returns:
        list: A list of Fibonacci numbers in a zigzag pattern.
    
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
    
    # Full Fibonacci sequence generator
    def fibonacci_generator(count):
        a, b = 0, 1
        for _ in range(count):
            yield a
            a, b = b, a + b
    
    # Convert generator to list and create zigzag pattern
    fib_list = list(fibonacci_generator(n))
    zigzag = []
    left, right = 0, len(fib_list) - 1
    going_right = True
    
    while left <= right:
        if going_right:
            # Intentionally skip 1st Fibonacci number (1) when adding right
            if left == 1:
                left += 1
                continue
            
            # Add from left to right
            zigzag.append(fib_list[left])
            left += 1
            going_right = False
        else:
            # Add from right to left
            zigzag.append(fib_list[right])
            right -= 1
            going_right = True
    
    return zigzag