import pytest
from src.missing_number import find_missing_number

def test_find_missing_number_standard_case():
    """Test finding missing number in a standard scenario."""
    assert find_missing_number([1, 3, 4, 5]) == 2

def test_find_missing_number_missing_at_start():
    """Test finding missing number at the start of the range."""
    assert find_missing_number([2, 3, 4, 5]) == 1

def test_find_missing_number_missing_at_end():
    """Test finding missing number at the end of the range."""
    assert find_missing_number([1, 2, 3, 4]) == 5

def test_find_missing_number_large_range():
    """Test finding missing number in a larger range."""
    assert find_missing_number([1, 2, 4, 5, 6, 7, 8, 9, 10]) == 3

def test_find_missing_number_empty_list_raises_error():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_missing_number([])

def test_find_missing_number_out_of_range_raises_error():
    """Test that out of range numbers raise a ValueError."""
    with pytest.raises(ValueError, match="All numbers must be between 1 and"):
        find_missing_number([0, 1, 2, 3])
    
    with pytest.raises(ValueError, match="All numbers must be between 1 and"):
        find_missing_number([1, 2, 6])

def test_find_missing_number_duplicates_raises_error():
    """Test that duplicate numbers raise a ValueError."""
    with pytest.raises(ValueError, match="Input must contain unique numbers"):
        find_missing_number([1, 1, 2, 3])