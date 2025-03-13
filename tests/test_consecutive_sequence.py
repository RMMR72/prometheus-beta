import pytest
from src.consecutive_sequence import find_longest_consecutive_sequence

def test_standard_case():
    assert find_longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) == [1, 2, 3, 4]

def test_empty_list():
    assert find_longest_consecutive_sequence([]) == []

def test_single_element():
    assert find_longest_consecutive_sequence([42]) == [42]

def test_all_duplicate_elements():
    assert find_longest_consecutive_sequence([1, 1, 1, 1]) == [1]

def test_unsorted_input():
    assert find_longest_consecutive_sequence([9, 1, 4, 7, 3, 2, 5, 6]) == [1, 2, 3, 4, 5, 6, 7]

def test_negative_numbers():
    assert find_longest_consecutive_sequence([-3, -2, -1, 0, 1]) == [-3, -2, -1, 0, 1]

def test_multiple_sequences():
    # Update to expect the longest consecutive sequence
    assert find_longest_consecutive_sequence([1, 2, 3, 10, 11, 12, 13]) == [10, 11, 12, 13]

def test_invalid_input_non_list():
    with pytest.raises(TypeError):
        find_longest_consecutive_sequence("not a list")

def test_invalid_input_non_integers():
    with pytest.raises(ValueError):
        find_longest_consecutive_sequence([1, 2, "3", 4])

def test_large_numbers():
    # Expect the first longest consecutive sequence
    result = find_longest_consecutive_sequence([1000000, 1000001, 1000002, 5, 6, 7])
    assert result == [5, 6, 7]  # Or [1000000, 1000001, 1000002], depending on implementation