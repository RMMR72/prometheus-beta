import pytest
from src.count_occurrences import count_occurrences

def test_count_occurrences_basic():
    """Test basic counting of element occurrences."""
    arr = [1, 2, 3, 2, 4, 2, 5]
    assert count_occurrences(arr, 2) == 3
    assert count_occurrences(arr, 1) == 1
    assert count_occurrences(arr, 6) == 0

def test_count_occurrences_different_types():
    """Test counting occurrences with different types of elements."""
    arr = [1, 'a', 2, 'a', 3, 'a']
    assert count_occurrences(arr, 'a') == 3
    assert count_occurrences(arr, 1) == 1
    assert count_occurrences(arr, 4) == 0

def test_count_occurrences_empty_list():
    """Test counting in an empty list."""
    arr = []
    assert count_occurrences(arr, 1) == 0
    assert count_occurrences(arr, 'a') == 0

def test_count_occurrences_invalid_input():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError, match="Input must be a list"):
        count_occurrences("not a list", 1)
    
    with pytest.raises(TypeError, match="Input must be a list"):
        count_occurrences(123, 1)
    
    with pytest.raises(TypeError, match="Input must be a list"):
        count_occurrences(None, 1)