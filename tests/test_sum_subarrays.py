import pytest
from src.sum_subarrays import sum_subarrays

def test_basic_functionality():
    """Test basic functionality with a simple list."""
    arr = [1, 2, 3]
    k = 2
    assert sum_subarrays(arr, k) == 21  # (1) + (2) + (3) + (1,2) + (2,3) + (1,2,3)

def test_empty_list():
    """Test with an empty list."""
    assert sum_subarrays([], 3) == 0

def test_zero_k():
    """Test when k is zero."""
    assert sum_subarrays([1, 2, 3], 0) == 0

def test_k_greater_than_list_length():
    """Test when k is larger than list length."""
    arr = [1, 2, 3]
    k = 5
    assert sum_subarrays(arr, k) == 21

def test_single_element_list():
    """Test with a single-element list."""
    assert sum_subarrays([5], 1) == 5

def test_invalid_input_types():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError, match="Input 'arr' must be a list"):
        sum_subarrays("not a list", 3)
    
    with pytest.raises(TypeError, match="Input 'k' must be an integer"):
        sum_subarrays([1, 2, 3], "2")

def test_negative_k():
    """Test error handling for negative k."""
    with pytest.raises(ValueError, match="Input 'k' must be non-negative"):
        sum_subarrays([1, 2, 3], -1)

def test_large_k():
    """Test with a large k."""
    arr = [1, 2, 3, 4, 5]
    k = 100
    assert sum_subarrays(arr, k) == 105  # Sum of all subarrays

def test_sorted_input():
    """Verify the function works with an already sorted input."""
    arr = [-3, -1, 0, 2, 4]
    k = 3
    # Calculates sum of all subarrays of length <= 3
    assert sum_subarrays(arr, k) == 77