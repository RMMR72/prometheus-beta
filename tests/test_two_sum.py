import pytest
from src.two_sum import has_two_sum

def test_two_sum_exists():
    """Test when two numbers sum to the target"""
    assert has_two_sum([1, 2, 3, 4], 7) == True
    assert has_two_sum([10, 15, 3, 7], 17) == True
    assert has_two_sum([-1, 5, 10, -3, 2], 7) == True

def test_two_sum_not_exists():
    """Test when no two numbers sum to the target"""
    assert has_two_sum([1, 2, 3, 4], 10) == False
    assert has_two_sum([1, 2, 3, 4], 0) == False

def test_edge_cases():
    """Test edge cases"""
    # Empty list
    assert has_two_sum([], 5) == False
    
    # Single element list
    assert has_two_sum([5], 10) == False
    
    # List with only one number that cannot sum to target
    assert has_two_sum([5], 5) == False

def test_duplicate_numbers():
    """Test list with duplicate numbers"""
    assert has_two_sum([3, 3], 6) == True
    assert has_two_sum([3, 3, 4], 6) == True
    assert has_two_sum([1, 2, 3, 3], 6) == True

def test_negative_numbers():
    """Test lists with negative numbers"""
    assert has_two_sum([-1, -2, 3, 4], 2) == True
    assert has_two_sum([-5, -2, -3, -1], -8) == True