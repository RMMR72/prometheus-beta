def fibonacci(n):
    """
    Compute the nth Fibonacci number using memoization.
    
    Args:
        n (int): The index of the Fibonacci number to compute (0-based).
    
    Returns:
        int: The nth Fibonacci number.
    
    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    
    # Memoization cache
    memo = {0: 0, 1: 1}
    
    # Compute Fibonacci numbers up to n
    def _fib(k):
        # Check if already memoized
        if k in memo:
            return memo[k]
        
        # Compute and memoize
        memo[k] = _fib(k-1) + _fib(k-2)
        return memo[k]
    
    return _fib(n)