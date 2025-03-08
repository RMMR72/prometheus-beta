import pytest
from src.anagram import isAnagram

def test_basic_anagrams():
    """Test basic anagram scenarios"""
    assert isAnagram("listen", "silent") == True
    assert isAnagram("triangle", "integral") == True
    assert isAnagram("hello", "world") == False

def test_case_insensitive():
    """Test that the function is case-insensitive"""
    assert isAnagram("Tea", "Eat") == True
    assert isAnagram("Debit Card", "Bad Credit") == True

def test_whitespace():
    """Test that whitespace is ignored"""
    assert isAnagram("rail safety", "fairy tales") == True
    assert isAnagram("   silent", "listen   ") == True

def test_empty_strings():
    """Test handling of empty strings"""
    assert isAnagram("", "") == True

def test_different_lengths():
    """Test strings of different lengths"""
    assert isAnagram("abc", "abcd") == False
    assert isAnagram("a", "") == False

def test_same_length_different_chars():
    """Test strings with same length but different characters"""
    assert isAnagram("abc", "def") == False

def test_repeated_characters():
    """Test strings with repeated characters"""
    assert isAnagram("aab", "aba") == True
    assert isAnagram("aab", "aaa") == False