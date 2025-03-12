import pytest
from src.anagram_counter import count_anagrams

def test_basic_anagram_count():
    """Test basic anagram counting for simple strings."""
    assert count_anagrams('abcde') == 15
    assert count_anagrams('aaa') == 3

def test_single_character_string():
    """Test string with a single character."""
    assert count_anagrams('a') == 1

def test_repeated_characters():
    """Test string with repeated characters."""
    assert count_anagrams('aaaa') == 4

def test_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be a non-empty string with lowercase English letters only"):
        count_anagrams('')
    
    with pytest.raises(ValueError, match="Input must be a non-empty string with lowercase English letters only"):
        count_anagrams('ABC')
    
    with pytest.raises(ValueError, match="Input must be a non-empty string with lowercase English letters only"):
        count_anagrams('ab1')

def test_longer_string():
    """Test a longer string with various anagram configurations."""
    assert count_anagrams('abcb') == 7