import pytest
from src.max_subarray_sum import max_subarray_sum

def test_positive_numbers():
    """Test max subarray sum with all positive numbers"""
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15

def test_mixed_numbers():
    """Test max subarray sum with mixed positive and negative numbers"""
    assert max_subarray_sum([1, -2, 3, 4, -1, 5]) == 11

def test_all_negative_numbers():
    """Test max subarray sum when all numbers are negative"""
    assert max_subarray_sum([-1, -2, -3, -4]) == -1

def test_single_element():
    """Test max subarray sum with a single element"""
    assert max_subarray_sum([42]) == 42

def test_invalid_input_empty_list():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        max_subarray_sum([])

def test_invalid_input_not_list():
    """Test that non-list input raises a TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        max_subarray_sum("not a list")

def test_zero_sum():
    """Test a list that results in zero sum"""
    assert max_subarray_sum([1, -1, 1, -1]) == 1

def test_complex_case():
    """Test a more complex case with larger numbers"""
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6