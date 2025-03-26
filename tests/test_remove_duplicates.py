import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic duplicate removal"""
    assert remove_duplicates([1, 2, 3, 2, 4, 1, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_order_preservation():
    """Test that original order of first occurrence is maintained"""
    assert remove_duplicates([5, 2, 3, 2, 5, 1, 4]) == [5, 2, 3, 1, 4]

def test_remove_duplicates_no_duplicates():
    """Test list with no duplicates"""
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_all_duplicates():
    """Test list with all duplicate values"""
    assert remove_duplicates([1, 1, 1, 1, 1]) == [1]

def test_remove_duplicates_empty_list():
    """Test empty list"""
    assert remove_duplicates([]) == []

def test_remove_duplicates_large_list():
    """Test a list with more than 10 unique integers"""
    test_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 20, 30, 40, 10]
    assert remove_duplicates(test_list) == [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def test_remove_duplicates_invalid_input_type():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates("not a list")

def test_remove_duplicates_invalid_element_type():
    """Test raising ValueError for non-integer elements"""
    with pytest.raises(ValueError, match="All elements must be integers"):
        remove_duplicates([1, 2, "3", 4, 5])

def test_remove_duplicates_mixed_duplicates():
    """Test removing duplicates with mixed positioning"""
    assert remove_duplicates([1, 2, 3, 1, 2, 4, 5, 3]) == [1, 2, 3, 4, 5]