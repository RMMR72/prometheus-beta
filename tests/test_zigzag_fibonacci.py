import pytest
from src.zigzag_fibonacci import generate_zigzag_fibonacci

def test_zigzag_fibonacci_basic():
    """Test basic functionality of zigzag Fibonacci generator."""
    assert generate_zigzag_fibonacci(1) == [0]
    assert generate_zigzag_fibonacci(2) == [0, 1]
    assert generate_zigzag_fibonacci(3) == [0, 2, 1]
    assert generate_zigzag_fibonacci(4) == [0, 2, 1, 3]
    assert generate_zigzag_fibonacci(5) == [0, 2, 1, 3, 5]

def test_zigzag_fibonacci_longer_sequence():
    """Test longer Fibonacci sequences in zigzag pattern."""
    result = generate_zigzag_fibonacci(7)
    assert result == [0, 2, 1, 3, 5, 8, 13]
    
    result = generate_zigzag_fibonacci(8)
    assert result == [0, 2, 1, 3, 5, 8, 13, 21]

def test_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        generate_zigzag_fibonacci(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        generate_zigzag_fibonacci(-1)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        generate_zigzag_fibonacci(1.5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        generate_zigzag_fibonacci("3")

def test_zigzag_pattern_alternation():
    """Verify the zigzag pattern alternation."""
    result = generate_zigzag_fibonacci(6)
    assert result == [0, 2, 1, 3, 5, 8]
    
    # Verify the directional changes
    assert result[0] == 0  # Start from beginning
    assert result[1] == 2  # Then next element
    assert result[2] == 1  # Then previous direction
    assert result[3] == 3  # Continue zigzag