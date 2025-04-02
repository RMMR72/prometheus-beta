import pytest
from src.counting_sort import counting_sort

def test_counting_sort_normal_case():
    """Test sorting a list of non-negative integers"""
    input_list = [4, 2, 2, 8, 3, 3, 1]
    assert counting_sort(input_list) == [1, 2, 2, 3, 3, 4, 8]

def test_counting_sort_empty_list():
    """Test sorting an empty list"""
    assert counting_sort([]) == []

def test_counting_sort_single_element():
    """Test sorting a list with a single element"""
    assert counting_sort([5]) == [5]

def test_counting_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert counting_sort(input_list) == input_list

def test_counting_sort_all_same_elements():
    """Test sorting a list with all identical elements"""
    input_list = [3, 3, 3, 3, 3]
    assert counting_sort(input_list) == input_list

def test_counting_sort_invalid_input_type():
    """Test error handling for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        counting_sort("not a list")

def test_counting_sort_negative_numbers():
    """Test error handling for negative numbers"""
    with pytest.raises(ValueError, match="Counting sort only works with non-negative integers"):
        counting_sort([1, 2, -3, 4])

def test_counting_sort_non_numeric():
    """Test error handling for non-numeric elements"""
    with pytest.raises(TypeError, match="List must contain comparable numeric values"):
        counting_sort([1, 2, 'a', 4])