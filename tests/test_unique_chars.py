import pytest
from src.unique_chars import extract_unique_chars

def test_extract_unique_chars_basic():
    assert extract_unique_chars("11223344") == "1234"
    assert extract_unique_chars("123456789") == "123456789"
    assert extract_unique_chars("000111222") == "012"

def test_extract_unique_chars_edge_cases():
    assert extract_unique_chars("") == ""  # Empty string
    assert extract_unique_chars("9") == "9"  # Single character
    assert extract_unique_chars("55555") == "5"  # Repeated single character

def test_extract_unique_chars_error_handling():
    # TypeError for non-string input
    with pytest.raises(TypeError, match="Input must be a string"):
        extract_unique_chars(12345)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        extract_unique_chars(None)
    
    # ValueError for non-numeric characters
    with pytest.raises(ValueError, match="Input must contain only numeric characters"):
        extract_unique_chars("123a456")
    
    with pytest.raises(ValueError, match="Input must contain only numeric characters"):
        extract_unique_chars("123.456")

def test_extract_unique_chars_order_preservation():
    # Ensure order of first appearance is preserved
    assert extract_unique_chars("41231231") == "4123"
    assert extract_unique_chars("91827364") == "91827364"