import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from list_mode import find_mode

def test_single_mode_integer():
    """Test finding a single mode with integer input."""
    assert find_mode([1, 2, 2, 3, 4]) == 2

def test_single_mode_float():
    """Test finding a single mode with float input."""
    assert find_mode([1.5, 2.3, 2.3, 3.7, 4.1]) == 2.3

def test_multiple_modes():
    """Test finding multiple modes."""
    assert sorted(find_mode([1, 2, 2, 3, 3, 4])) == [2, 3]

def test_empty_list():
    """Test behavior with an empty list."""
    assert find_mode([]) == []

def test_all_unique_elements():
    """Test list where all elements have the same frequency."""
    assert sorted(find_mode([1, 2, 3, 4])) == [1, 2, 3, 4]

def test_input_type_error():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_mode("not a list")

def test_invalid_numeric_input():
    """Test raising ValueError for non-numeric list."""
    with pytest.raises(ValueError, match="List must contain only numeric values"):
        find_mode([1, 2, "three", 4])

def test_single_element_list():
    """Test mode for a list with a single element."""
    assert find_mode([42]) == 42