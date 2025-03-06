import pytest
from src.find_max import find_max

def test_find_max_positive_numbers():
    """Test finding max in an array of positive numbers."""
    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([10, 5, 8, 12, 3]) == 12

def test_find_max_negative_numbers():
    """Test finding max in an array of negative numbers."""
    assert find_max([-1, -2, -3, -4, -5]) == -1
    assert find_max([-10, -5, -8, -12, -3]) == -3

def test_find_max_mixed_numbers():
    """Test finding max in an array with mixed positive and negative numbers."""
    assert find_max([-10, 0, 5, -5, 10]) == 10
    assert find_max([-100, 100, 0]) == 100

def test_find_max_floating_point():
    """Test finding max with floating point numbers."""
    assert find_max([1.5, 2.7, 3.2, 0.1]) == 3.2
    assert find_max([-1.5, -2.7, -0.1]) == -0.1

def test_find_max_single_element():
    """Test finding max in a single-element array."""
    assert find_max([42]) == 42
    assert find_max([-42]) == -42

def test_find_max_empty_array():
    """Test that an empty array raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot find maximum of an empty array"):
        find_max([])

def test_find_max_invalid_input():
    """Test that non-list inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_max(42)
    with pytest.raises(TypeError, match="Input must be a list"):
        find_max("not a list")

def test_find_max_non_numeric():
    """Test that non-numeric elements raise a TypeError."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_max([1, 2, '3'])
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_max([1, 2, [3]])