import pytest
from src.switch_cases import switch_cases

def test_switch_cases_basic():
    """Test basic case swapping functionality."""
    assert switch_cases("Hello", "world") == "hELLO"
    assert switch_cases("PYTHON", "code") == "code"

def test_switch_cases_different_lengths():
    """Test behavior with strings of different lengths."""
    assert switch_cases("Hello", "w") == "h"
    assert switch_cases("a", "WORLD") == "A"

def test_switch_cases_all_cases():
    """Test various case combinations."""
    assert switch_cases("AbCdE", "UPPER") == "aBcDe"
    assert switch_cases("AbCdE", "lower") == "aBcDe"

def test_switch_cases_empty_strings():
    """Test behavior with empty strings."""
    assert switch_cases("", "") == ""
    assert switch_cases("Hello", "") == ""
    assert switch_cases("", "World") == ""

def test_switch_cases_non_string_input():
    """Test error handling for non-string inputs."""
    with pytest.raises(TypeError):
        switch_cases(123, "abc")
    with pytest.raises(TypeError):
        switch_cases("abc", None)
    with pytest.raises(TypeError):
        switch_cases(None, None)

def test_switch_cases_unicode():
    """Test handling of unicode characters."""
    assert switch_cases("Héllö", "WORLD") == "hÉLLÖ"