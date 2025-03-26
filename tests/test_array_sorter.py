import pytest
from src.array_sorter import sort_array_with_even_squares

def test_basic_sorting():
    """Test basic functionality of the sorting function."""
    input_arr = [5, 3, 2, 4, 1]
    expected = [1, 3, 4, 5, 16]
    assert sort_array_with_even_squares(input_arr) == expected

def test_all_even_numbers():
    """Test a list with only even numbers."""
    input_arr = [6, 2, 4, 8]
    expected = [2, 4, 6, 64]
    assert sort_array_with_even_squares(input_arr) == expected

def test_all_odd_numbers():
    """Test a list with only odd numbers."""
    input_arr = [5, 3, 7, 1]
    expected = [1, 3, 5, 7]
    assert sort_array_with_even_squares(input_arr) == expected

def test_empty_list():
    """Test an empty list."""
    input_arr = []
    expected = []
    assert sort_array_with_even_squares(input_arr) == expected

def test_negative_numbers():
    """Test list with negative numbers."""
    input_arr = [-2, 5, -4, 3, 1]
    expected = [1, 3, 5, 16, 16]
    assert sort_array_with_even_squares(input_arr) == expected

def test_float_input():
    """Test list with floating point numbers."""
    input_arr = [2.5, 2.0, 4.0, 1.5]
    expected = [1.5, 2.0, 2.5, 16.0]
    assert sort_array_with_even_squares(input_arr) == expected

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError):
        sort_array_with_even_squares("not a list")

def test_invalid_element_type():
    """Test that a ValueError is raised for non-numeric elements."""
    with pytest.raises(ValueError):
        sort_array_with_even_squares([1, 2, "three"])