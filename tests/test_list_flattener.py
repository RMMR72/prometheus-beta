import pytest
from src.list_flattener import flatten_nested_list

def test_flatten_simple_list():
    """Test flattening a simple nested list."""
    assert flatten_nested_list([1, 2, 3]) == [1, 2, 3]

def test_flatten_nested_list():
    """Test flattening a nested list with multiple levels."""
    assert flatten_nested_list([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]

def test_flatten_empty_list():
    """Test flattening an empty list."""
    assert flatten_nested_list([]) == []

def test_flatten_deeply_nested_list():
    """Test flattening a deeply nested list."""
    nested = [1, [2, [3, [4, [5]]]], 6]
    assert flatten_nested_list(nested) == [1, 2, 3, 4, 5, 6]

def test_flatten_mixed_list():
    """Test flattening a list with mixed types of nested lists."""
    nested = [1, [], [2, 3], [[4]], [5, [6]]]
    assert flatten_nested_list(nested) == [1, 2, 3, 4, 5, 6]

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_nested_list("not a list")
    
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_nested_list(123)
    
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_nested_list(None)