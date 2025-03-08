import pytest
from src.triangular_numbers import count_triangular_numbers

def test_count_triangular_numbers_basic():
    """Test basic functionality of counting triangular numbers."""
    assert count_triangular_numbers(10) == 4  # 1, 3, 6, 10
    assert count_triangular_numbers(1) == 1   # only 1
    assert count_triangular_numbers(3) == 2   # 1, 3
    assert count_triangular_numbers(6) == 3   # 1, 3, 6

def test_count_triangular_numbers_zero():
    """Test behavior with zero input."""
    assert count_triangular_numbers(0) == 0

def test_count_triangular_numbers_large():
    """Test with a larger number."""
    assert count_triangular_numbers(100) == 13

def test_count_triangular_numbers_invalid_input():
    """Test error handling for invalid inputs."""
    # Test negative input
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        count_triangular_numbers(-1)
    
    # Test non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        count_triangular_numbers(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        count_triangular_numbers("10")

def test_count_triangular_numbers_edge_cases():
    """Test various edge cases."""
    # Special cases around the first few triangular numbers
    assert count_triangular_numbers(1) == 1   # First triangular number
    assert count_triangular_numbers(2) == 1   # Between 1st and 2nd
    assert count_triangular_numbers(3) == 2   # Exactly 2nd triangular number
    assert count_triangular_numbers(5) == 2   # Between 2nd and 3rd