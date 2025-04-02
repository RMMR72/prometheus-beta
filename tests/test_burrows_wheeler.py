import pytest
from src.burrows_wheeler import burrows_wheeler_transform, inverse_burrows_wheeler_transform

def test_burrows_wheeler_transform_simple():
    """Test basic Burrows-Wheeler Transform"""
    text = "banana"
    expected_bwt = "annb$aa"
    assert burrows_wheeler_transform(text) == expected_bwt

def test_inverse_burrows_wheeler_transform_simple():
    """Test recovering original text from BWT"""
    text = "banana"
    bwt = burrows_wheeler_transform(text)
    assert inverse_burrows_wheeler_transform(bwt) == text

def test_bwt_symmetry():
    """Test that BWT and inverse BWT are symmetric"""
    test_cases = [
        "hello",
        "world",
        "python",
        "algorithm",
        "transformation"
    ]
    
    for case in test_cases:
        bwt = burrows_wheeler_transform(case)
        recovered = inverse_burrows_wheeler_transform(bwt)
        assert recovered == case, f"Failed for input: {case}"

def test_bwt_edge_cases():
    """Test edge cases for BWT"""
    # Single character
    assert burrows_wheeler_transform("a") == "a$"
    assert inverse_burrows_wheeler_transform("a$") == "a"

def test_bwt_error_handling():
    """Test error handling for invalid inputs"""
    # Empty string
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        burrows_wheeler_transform("")
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        inverse_burrows_wheeler_transform("")
    
    # Non-string input
    with pytest.raises(TypeError, match="Input must be a string"):
        burrows_wheeler_transform(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        inverse_burrows_wheeler_transform(456)

def test_bwt_special_characters():
    """Test BWT with strings containing special characters"""
    test_cases = [
        "hello, world!",
        "123 456",
        "a@b#c$d%e"
    ]
    
    for case in test_cases:
        bwt = burrows_wheeler_transform(case)
        recovered = inverse_burrows_wheeler_transform(bwt)
        assert recovered == case, f"Failed for input: {case}"