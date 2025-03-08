import pytest
from src.even_indexed_sum import sum_even_indexed_elements

def test_sum_even_indexed_elements_normal_list():
    """Test with a list of positive integers."""
    assert sum_even_indexed_elements([1, 2, 3, 4, 5]) == 9

def test_sum_even_indexed_elements_mixed_signs():
    """Test with a list containing positive and negative integers."""
    assert sum_even_indexed_elements([-1, 2, -3, 4, -5]) == -9

def test_sum_even_indexed_elements_empty_list():
    """Test with an empty list."""
    assert sum_even_indexed_elements([]) == 0

def test_sum_even_indexed_elements_single_element():
    """Test with a single-element list."""
    assert sum_even_indexed_elements([42]) == 42

def test_sum_even_indexed_elements_all_zeros():
    """Test with a list of zeros."""
    assert sum_even_indexed_elements([0, 10, 0, 20, 0]) == 0

def test_sum_even_indexed_elements_type_error():
    """Test that the function raises a TypeError for non-list input."""
    with pytest.raises(TypeError):
        sum_even_indexed_elements("not a list")

def test_sum_even_indexed_elements_nested_list():
    """Test that the function works with nested lists."""
    assert sum_even_indexed_elements([1, [2], 3, [4], 5]) == 9