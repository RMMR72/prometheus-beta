import pytest
import time
from src.sleep_sort import sleep_sort

def test_basic_integer_sorting():
    """Test sorting of basic integer list"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    expected = sorted(input_list)
    result = sleep_sort(input_list)
    assert result == expected, f"Expected {expected}, got {result}"

def test_float_sorting():
    """Test sorting of float numbers"""
    input_list = [3.14, 1.41, 2.71, 0.58]
    expected = sorted(input_list)
    result = sleep_sort(input_list)
    assert result == expected, f"Expected {expected}, got {result}"

def test_empty_list():
    """Test sorting of empty list"""
    assert sleep_sort([]) == [], "Empty list should return empty list"

def test_single_element_list():
    """Test sorting of single-element list"""
    input_list = [42]
    assert sleep_sort(input_list) == input_list, "Single element list should remain unchanged"

def test_negative_numbers_raise_error():
    """Test that negative numbers raise a ValueError"""
    with pytest.raises(ValueError, match="Sleep Sort does not support negative numbers"):
        sleep_sort([-1, 2, 3])

def test_non_numeric_types_raise_error():
    """Test that non-numeric types raise a TypeError"""
    with pytest.raises(TypeError, match="Input must contain only numeric types"):
        sleep_sort([1, 'a', 3])

def test_sorting_performance():
    """Verify that sorting is relatively quick"""
    input_list = [0.1, 0.5, 0.3, 0.2, 0.4]
    start_time = time.time()
    result = sleep_sort(input_list)
    end_time = time.time()
    
    # Verify sorted result
    assert result == sorted(input_list), "Result should be sorted"
    
    # Verify total time is reasonable (< 1 second)
    assert end_time - start_time < 1, "Sorting time should be relatively quick"