import pytest
from src.local_max import find_local_max

def test_multiple_local_max():
    """Test array with multiple local maximum values"""
    arr = [1, 3, 2, 4, 1, 5, 3]
    assert set(find_local_max(arr)) == {1, 3, 5}

def test_single_element():
    """Test array with a single element"""
    arr = [42]
    assert find_local_max(arr) == [0]

def test_sorted_ascending():
    """Test sorted ascending array"""
    arr = [1, 2, 3, 4, 5]
    assert find_local_max(arr) == [4]

def test_sorted_descending():
    """Test sorted descending array"""
    arr = [5, 4, 3, 2, 1]
    assert find_local_max(arr) == [0]

def test_all_equal():
    """Test array with all equal elements"""
    arr = [2, 2, 2, 2]
    assert find_local_max(arr) == []

def test_error_empty_list():
    """Test error handling for empty list"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_local_max([])

def test_error_invalid_input():
    """Test error handling for invalid input type"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_local_max("not a list")

def test_alternating_peak_valley():
    """Test alternating peak and valley array"""
    arr = [1, 3, 1, 4, 1, 5, 1]
    assert set(find_local_max(arr)) == {1, 3, 5}