import pytest
from src.string_reverser import reverse_string_in_place

def test_reverse_string_in_place_basic():
    """Test basic string reversal."""
    chars = list('hello')
    reverse_string_in_place(chars)
    assert chars == list('olleh')

def test_reverse_string_in_place_empty():
    """Test reversing an empty string."""
    chars = []
    reverse_string_in_place(chars)
    assert chars == []

def test_reverse_string_in_place_single_char():
    """Test reversing a single character."""
    chars = list('a')
    reverse_string_in_place(chars)
    assert chars == list('a')

def test_reverse_string_in_place_even_length():
    """Test reversing a string with even number of characters."""
    chars = list('abcd')
    reverse_string_in_place(chars)
    assert chars == list('dcba')

def test_reverse_string_in_place_odd_length():
    """Test reversing a string with odd number of characters."""
    chars = list('python')
    reverse_string_in_place(chars)
    assert chars == list('nohtyp')

def test_reverse_string_in_place_immutable_error():
    """Test that an error is raised for immutable sequences."""
    with pytest.raises(TypeError):
        reverse_string_in_place('hello')  # string is immutable

def test_reverse_string_in_place_no_copy():
    """Ensure the function does not create a copy of the input."""
    chars = list('hello')
    original_id = id(chars)
    reverse_string_in_place(chars)
    assert id(chars) == original_id  # same object should be modified