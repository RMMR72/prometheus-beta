import pytest
from src.closest_pair_sum import find_closest_pair_sum

def test_basic_functionality():
    """Test finding the closest pair sum in a normal scenario"""
    arr = [1, 2, 3, 4, 5]
    target = 7
    result = find_closest_pair_sum(arr, target)
    assert result == (2, 5) or result == (3, 4)

def test_negative_numbers():
    """Test with negative numbers"""
    arr = [-1, -2, 1, 2, 3]
    target = 0
    result = find_closest_pair_sum(arr, target)
    assert result == (-1, 1)

def test_floating_point_numbers():
    """Test with floating point numbers"""
    arr = [1.5, 2.5, 3.5, 4.5]
    target = 6
    result = find_closest_pair_sum(arr, target)
    assert result == (1.5, 4.5)

def test_multiple_closest_pairs():
    """Test when multiple pairs have equal closeness"""
    arr = [1, 4, 2, 3, 6]
    target = 5
    result = find_closest_pair_sum(arr, target)
    assert result == (1, 4)  # First occurrence

def test_single_element_list():
    """Test with a list containing fewer than 2 elements"""
    arr = [1]
    target = 5
    result = find_closest_pair_sum(arr, target)
    assert result is None

def test_empty_list():
    """Test with an empty list"""
    arr = []
    target = 5
    result = find_closest_pair_sum(arr, target)
    assert result is None

def test_invalid_input_type():
    """Test with invalid input type"""
    with pytest.raises(TypeError):
        find_closest_pair_sum("not a list", 5)

def test_invalid_target_type():
    """Test with invalid target type"""
    with pytest.raises(TypeError):
        find_closest_pair_sum([1, 2, 3], "not a number")

def test_non_numeric_list():
    """Test with list containing non-numeric elements"""
    with pytest.raises(ValueError):
        find_closest_pair_sum([1, 2, 'a'], 5)