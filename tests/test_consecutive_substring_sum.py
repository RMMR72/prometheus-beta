import pytest
from src.consecutive_substring_sum import max_consecutive_substring_sum

def test_basic_consecutive_sequence():
    assert max_consecutive_substring_sum("abcde") == 495  # a(97) + b(98) + c(99) + d(100) + e(101)

def test_multiple_consecutive_sequences():
    assert max_consecutive_substring_sum("abcdexyz") == 495  # first sequence max

def test_single_character():
    assert max_consecutive_substring_sum("a") == 97  # ASCII value of 'a'

def test_non_consecutive_characters():
    assert max_consecutive_substring_sum("aceg") == 103  # largest character

def test_repeated_consecutive_sequence():
    assert max_consecutive_substring_sum("abcabcde") == 495  # full consecutive sequence

def test_input_validation():
    with pytest.raises(TypeError):
        max_consecutive_substring_sum(123)
    
    with pytest.raises(ValueError):
        max_consecutive_substring_sum("")

def test_mixed_case_sequence():
    assert max_consecutive_substring_sum("AbCdEf") == 597  # a(97) + b(98) + c(99) + d(100) + e(101) + f(102)

def test_special_characters_consecutive():
    assert max_consecutive_substring_sum("!\"#$%&") == 213  # Multiple consecutive ASCII chars

def test_unicode_characters():
    assert max_consecutive_substring_sum("αβγ") == 2838  # Sum of consecutive Unicode chars