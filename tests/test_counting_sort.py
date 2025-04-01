import pytest
from src.counting_sort import counting_sort

def test_basic_sorting():
    """Test basic sorting of a list of integers."""
    assert counting_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_already_sorted():
    """Test sorting an already sorted list."""
    assert counting_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_reverse_sorted():
    """Test sorting a reverse-sorted list."""
    assert counting_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_empty_list():
    """Test sorting an empty list."""
    assert counting_sort([]) == []

def test_single_element():
    """Test sorting a list with a single element."""
    assert counting_sort([42]) == [42]

def test_list_with_zeros():
    """Test sorting a list with zeros."""
    assert counting_sort([0, 0, 0, 0]) == [0, 0, 0, 0]

def test_invalid_input_type():
    """Test that a non-list input raises a TypeError."""
    with pytest.raises(TypeError):
        counting_sort("not a list")

def test_negative_numbers():
    """Test that negative numbers raise a ValueError."""
    with pytest.raises(ValueError):
        counting_sort([1, 2, -3, 4])

def test_non_integer_elements():
    """Test that non-integer elements raise a ValueError."""
    with pytest.raises(ValueError):
        counting_sort([1, 2, 3.14, 4])

def test_large_range():
    """Test sorting a list with a large range of values."""
    test_list = [1000, 0, 500, 250, 750]
    assert counting_sort(test_list) == [0, 250, 500, 750, 1000]