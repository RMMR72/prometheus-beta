import pytest
from src.fibonacci import fibonacci

def test_fibonacci_base_cases():
    """Test base cases of Fibonacci sequence."""
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1

def test_fibonacci_known_values():
    """Test known Fibonacci numbers."""
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

def test_fibonacci_larger_numbers():
    """Test larger Fibonacci numbers."""
    assert fibonacci(10) == 55
    assert fibonacci(20) == 6765

def test_fibonacci_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Negative number should raise ValueError
    with pytest.raises(ValueError, match="Fibonacci is not defined for negative numbers"):
        fibonacci(-1)
    
    # Non-integer input should raise TypeError
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci("5")

def test_fibonacci_performance():
    """Verify that repeated calls don't recompute values."""
    # This test checks if memoization works by ensuring quick computation of a large number
    import time
    
    start = time.time()
    result1 = fibonacci(35)
    first_call_time = time.time() - start
    
    start = time.time()
    result2 = fibonacci(35)
    second_call_time = time.time() - start
    
    # Verify the result is the same
    assert result1 == 9227465
    assert result1 == result2
    
    # Second call should be much faster due to memoization
    # Note: This is a probabilistic check and might need adjustment based on system
    assert second_call_time < first_call_time * 0.1