import pytest
from src.magic_square_validator import is_magic_square

def test_valid_magic_square():
    """Test a known valid magic square arrangement"""
    assert is_magic_square([4,9,2,3,5,7,8,1,6,0]) == True

def test_invalid_magic_square_wrong_length():
    """Test input with incorrect number of elements"""
    assert is_magic_square([1,2,3,4,5,6,7,8]) == False
    assert is_magic_square([1,2,3,4,5,6,7,8,9,10,11]) == False

def test_invalid_magic_square_non_integers():
    """Test input with non-integer elements"""
    assert is_magic_square([1,2,3,4,5,6,7,8,9,'a']) == False
    assert is_magic_square([1,2,3,4,5,6,7,8,9,1.5]) == False

def test_invalid_magic_square_out_of_range():
    """Test input with numbers outside 1-9 range"""
    assert is_magic_square([0,1,2,3,4,5,6,7,8,9]) == False
    assert is_magic_square([10,1,2,3,4,5,6,7,8,9]) == False

def test_invalid_magic_square_duplicate_numbers():
    """Test input with duplicate numbers"""
    assert is_magic_square([1,1,2,3,4,5,6,7,8,9]) == False

def test_non_magic_square_arrangement():
    """Test an arrangement that doesn't form a magic square"""
    # This is a specific sequence that uses 1-9 but isn't a magic square
    assert is_magic_square([1,2,3,4,5,6,7,8,9,0]) == False

def test_edge_case_empty_list():
    """Test empty list input"""
    assert is_magic_square([]) == False

def test_various_valid_magic_squares():
    """Test multiple valid magic square arrangements"""
    valid_squares = [
        [4,9,2,3,5,7,8,1,6,0],
        [2,7,6,9,5,1,4,3,8,0],
        [8,1,6,3,5,7,4,9,2,0]
    ]
    for square in valid_squares:
        assert is_magic_square(square) == True