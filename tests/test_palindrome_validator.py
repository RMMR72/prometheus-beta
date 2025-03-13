import pytest
from src.palindrome_validator import is_palindrome

def test_classic_palindromes():
    """Test classic palindrome scenarios."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True

def test_palindrome_with_spaces_and_punctuation():
    """Test palindromes with spaces and punctuation."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_case_insensitive_palindromes():
    """Test case-insensitive palindrome detection."""
    assert is_palindrome("Able was I ere I saw Elba") == True

def test_empty_and_single_char_strings():
    """Test edge cases with empty and single character strings."""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True

def test_non_palindromes():
    """Test various non-palindrome strings."""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_numeric_palindromes():
    """Test numeric palindromes."""
    assert is_palindrome("12321") == True
    assert is_palindrome("123 321") == True
    assert is_palindrome("12345") == False

def test_mixed_alphanumeric_palindromes():
    """Test mixed alphanumeric palindromes."""
    assert is_palindrome("a1b2c33c2b1a") == True
    assert is_palindrome("a1b2c3") == False

def test_whitespace_only_strings():
    """Test strings with only whitespace."""
    assert is_palindrome("   ") == True
    assert is_palindrome("\t\n ") == True