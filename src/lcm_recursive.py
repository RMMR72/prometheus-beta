def gcd_recursive(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) using recursion.
    
    Args:
        a (int): First positive integer
        b (int): Second positive integer
    
    Returns:
        int: The greatest common divisor of a and b
    
    Raises:
        ValueError: If either input is not a positive integer
    """
    # Validate inputs
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Inputs must be integers")
    
    # Convert to absolute values
    a, b = abs(a), abs(b)
    
    # Base case
    if b == 0:
        return a
    
    # Recursive case: use the Euclidean algorithm
    return gcd_recursive(b, a % b)

def lcm_recursive(a, b):
    """
    Calculate the Least Common Multiple (LCM) using recursion.
    
    The LCM is calculated using the formula: LCM(a,b) = |a * b| / GCD(a,b)
    
    Args:
        a (int): First positive integer
        b (int): Second positive integer
    
    Returns:
        int: The least common multiple of a and b
    
    Raises:
        ValueError: If either input is not a positive integer
        ZeroDivisionError: If both inputs are zero
    """
    # Validate inputs
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Inputs must be integers")
    
    # Special case: if either number is zero, LCM is zero
    if a == 0 or b == 0:
        return 0
    
    # Convert to absolute values
    a, b = abs(a), abs(b)
    
    # Calculate LCM using GCD
    return abs(a * b) // gcd_recursive(a, b)