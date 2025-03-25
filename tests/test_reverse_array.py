import pytest
from src.reverse_array import reverse_integer_array

def test_reverse_normal_array():
    """Test reversing a normal integer array."""
    input_arr = [1, 2, 3, 4, 5]
    expected = [5, 4, 3, 2, 1]
    assert reverse_integer_array(input_arr) == expected

def test_reverse_empty_array():
    """Test reversing an empty array."""
    assert reverse_integer_array([]) == []

def test_reverse_single_element_array():
    """Test reversing an array with a single element."""
    input_arr = [42]
    assert reverse_integer_array(input_arr) == [42]

def test_reverse_negative_numbers():
    """Test reversing an array with negative numbers."""
    input_arr = [-1, -2, -3, -4, -5]
    expected = [-5, -4, -3, -2, -1]
    assert reverse_integer_array(input_arr) == expected

def test_raise_non_list_input():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        reverse_integer_array(42)

def test_raise_non_integer_elements():
    """Test that a TypeError is raised for list with non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        reverse_integer_array([1, 2, '3', 4, 5])

def test_original_array_unchanged():
    """Ensure the original array is not modified."""
    input_arr = [1, 2, 3, 4, 5]
    reversed_arr = reverse_integer_array(input_arr)
    assert input_arr == [1, 2, 3, 4, 5]  # Original array should remain unchanged
    assert reversed_arr == [5, 4, 3, 2, 1]  # Reversed array should be correct