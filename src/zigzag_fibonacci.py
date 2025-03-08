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
    
    # Initialize Fibonacci sequence
    fib = [0, 1]
    
    # Generate remaining Fibonacci numbers
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    
    # Create zigzag pattern
    zigzag = []
    left = 0
    right = len(fib) - 1
    going_right = True
    
    while left <= right:
        if going_right:
            # Add from left to right
            while left <= right:
                zigzag.append(fib[left])
                left += 1
                going_right = False
        else:
            # Add from right to left
            while right >= left:
                zigzag.append(fib[right])
                right -= 1
                going_right = True
    
    return zigzag