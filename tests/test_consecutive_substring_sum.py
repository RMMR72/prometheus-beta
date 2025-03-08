import pytest
from src.consecutive_substring_sum import max_consecutive_substring_sum

def test_basic_consecutive_sequence():
    assert max_consecutive_substring_sum("abcde") == 495  # a(97) + b(98) + c(99) + d(100) + e(101)

def test_multiple_consecutive_sequences():
    assert max_consecutive_substring_sum("abcdexyz") == 495  # first sequence max

def test_single_character():
    assert max_consecutive_substring_sum("a") == 97  # ASCII value of 'a'

def test_non_consecutive_characters():
    assert max_consecutive_substring_sum("aceg") == 97  # just first character

def test_repeated_consecutive_sequence():
    assert max_consecutive_substring_sum("abcabcde") == 395  # c(99) + d(100) + e(101)

def test_input_validation():
    with pytest.raises(TypeError):
        max_consecutive_substring_sum(123)
    
    with pytest.raises(ValueError):
        max_consecutive_substring_sum("")

def test_mixed_case_sequence():
    assert max_consecutive_substring_sum("AbCdEf") == 395  # C(67) + D(68) + E(69) + F(70)

def test_special_characters_consecutive():
    assert max_consecutive_substring_sum("!\"#$%&") == 263  # "#(35) + $(36) + %(37) + &(38)

def test_unicode_characters():
    assert max_consecutive_substring_sum("αβγ") == 945  # α(945) + β(946) + γ(947)