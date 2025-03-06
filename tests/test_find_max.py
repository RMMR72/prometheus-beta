import pytest
from src.find_max import find_max_number

def test_find_max_positive_numbers():
    """Test finding max in a list of positive numbers."""
    assert find_max_number([1, 2, 3, 4, 5]) == 5
    assert find_max_number([10, 5, 8, 3]) == 10

def test_find_max_negative_numbers():
    """Test finding max in a list of negative numbers."""
    assert find_max_number([-1, -2, -3, -4, -5]) == -1
    assert find_max_number([-10, -5, -8, -3]) == -3

def test_find_max_mixed_numbers():
    """Test finding max in a list with mixed positive and negative numbers."""
    assert find_max_number([-1, 0, 1, 2]) == 2
    assert find_max_number([-10, 5, 0, -5]) == 5

def test_find_max_float_numbers():
    """Test finding max in a list with floating point numbers."""
    assert find_max_number([1.5, 2.7, 3.2, 0.1]) == 3.2
    assert find_max_number([-1.5, 2.7, -3.2, 0.1]) == 2.7

def test_find_max_single_element():
    """Test finding max in a list with a single element."""
    assert find_max_number([42]) == 42
    assert find_max_number([-42]) == -42

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot find maximum of an empty list"):
        find_max_number([])

def test_non_list_input_raises_error():
    """Test that non-list inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_max_number("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        find_max_number(123)

def test_non_numeric_elements_raises_error():
    """Test that lists with non-numeric elements raise a TypeError."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_max_number([1, 2, 'three', 4])
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_max_number([1, 2, None, 4])