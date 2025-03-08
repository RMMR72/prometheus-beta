import pytest
from src.lcs import longest_common_subsequence_length

def test_basic_lcs():
    assert longest_common_subsequence_length("ABCDGH", "AEDFHR") == 3
    assert longest_common_subsequence_length("AGGTAB", "GXTXAYB") == 4

def test_empty_strings():
    assert longest_common_subsequence_length("", "") == 0
    assert longest_common_subsequence_length("ABC", "") == 0
    assert longest_common_subsequence_length("", "XYZ") == 0

def test_identical_strings():
    assert longest_common_subsequence_length("HELLO", "HELLO") == 5
    assert longest_common_subsequence_length("", "") == 0

def test_no_common_subsequence():
    assert longest_common_subsequence_length("ABC", "XYZ") == 0

def test_partial_match():
    assert longest_common_subsequence_length("ABCBDAB", "BDCABA") == 4

def test_different_length_strings():
    assert longest_common_subsequence_length("ABCD", "AD") == 2
    assert longest_common_subsequence_length("AD", "ABCD") == 2

def test_case_sensitivity():
    assert longest_common_subsequence_length("AbC", "abc") == 0

def test_input_types():
    with pytest.raises(TypeError):
        longest_common_subsequence_length(None, "ABC")
    with pytest.raises(TypeError):
        longest_common_subsequence_length("ABC", None)