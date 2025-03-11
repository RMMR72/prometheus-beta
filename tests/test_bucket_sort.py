import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from bucket_sort import bucket_sort

def test_basic_sorting():
    """Test basic sorting of a list of numbers"""
    input_list = [0.5, 0.3, 0.8, 0.1, 0.4]
    result = bucket_sort(input_list)
    assert result == sorted(input_list)

def test_integer_sorting():
    """Test sorting of integer list"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    result = bucket_sort(input_list)
    assert result == sorted(input_list)

def test_mixed_numeric_sorting():
    """Test sorting of mixed numeric types"""
    input_list = [5.5, 3, 2.1, 4, 7.7]
    result = bucket_sort(input_list)
    assert result == sorted(input_list)

def test_already_sorted_list():
    """Test sorting of an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    result = bucket_sort(input_list)
    assert result == input_list

def test_reverse_sorted_list():
    """Test sorting of a reverse-sorted list"""
    input_list = [5, 4, 3, 2, 1]
    result = bucket_sort(input_list)
    assert result == sorted(input_list)

def test_single_element_list():
    """Test sorting of a single-element list"""
    input_list = [42]
    result = bucket_sort(input_list)
    assert result == input_list

def test_duplicate_elements():
    """Test sorting of a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = bucket_sort(input_list)
    assert result == sorted(input_list)

def test_custom_num_buckets():
    """Test sorting with a custom number of buckets"""
    input_list = [0.1, 0.5, 0.2, 0.9, 0.3, 0.7]
    result = bucket_sort(input_list, num_buckets=3)
    assert result == sorted(input_list)

def test_large_spread_of_numbers():
    """Test sorting of numbers with a large spread"""
    input_list = [1000, 1, 10000, 50, 100, 10]
    result = bucket_sort(input_list)
    assert result == sorted(input_list)

def test_invalid_input_type():
    """Test error handling for non-list input"""
    with pytest.raises(TypeError):
        bucket_sort("not a list")

def test_non_numeric_input():
    """Test error handling for list with non-numeric elements"""
    with pytest.raises(TypeError):
        bucket_sort([1, 2, 'a', 3])

def test_empty_list():
    """Test error handling for empty list"""
    with pytest.raises(ValueError):
        bucket_sort([])