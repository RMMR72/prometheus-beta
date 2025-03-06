import pytest
from src.fibonacci import generate_fibonacci

def test_fibonacci_zero_terms():
    """Test generating 0 terms."""
    assert generate_fibonacci(0) == []

def test_fibonacci_one_term():
    """Test generating 1 term."""
    assert generate_fibonacci(1) == [0]

def test_fibonacci_two_terms():
    """Test generating 2 terms."""
    assert generate_fibonacci(2) == [0, 1]

def test_fibonacci_multiple_terms():
    """Test generating multiple terms."""
    assert generate_fibonacci(5) == [0, 1, 1, 2, 3]
    assert generate_fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]

def test_fibonacci_negative_input():
    """Test that negative input raises ValueError."""
    with pytest.raises(ValueError, match="Number of terms must be non-negative"):
        generate_fibonacci(-1)

def test_fibonacci_invalid_input_type():
    """Test that non-integer input raises TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_fibonacci("5")
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_fibonacci(5.5)
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_fibonacci(None)