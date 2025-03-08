import pytest
from src.matrix_search import find_matrix_coordinates

def test_find_matrix_coordinates_basic():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert find_matrix_coordinates(matrix, 5) == (1, 1)
    assert find_matrix_coordinates(matrix, 1) == (0, 0)
    assert find_matrix_coordinates(matrix, 9) == (2, 2)

def test_find_matrix_coordinates_not_found():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert find_matrix_coordinates(matrix, 10) is None

def test_find_matrix_coordinates_first_occurrence():
    matrix = [
        [1, 2, 3],
        [4, 5, 3],
        [7, 8, 3]
    ]
    assert find_matrix_coordinates(matrix, 3) == (0, 2)

def test_find_matrix_coordinates_invalid_input():
    # Test empty matrix
    with pytest.raises(ValueError, match="Input must be a non-empty matrix"):
        find_matrix_coordinates([], 5)
    
    # Test non-list input
    with pytest.raises(ValueError, match="Input must be a non-empty matrix"):
        find_matrix_coordinates(None, 5)
    
    # Test non-2D matrix
    with pytest.raises(TypeError, match="Input must be a 2D matrix"):
        find_matrix_coordinates([1, 2, 3], 5)
    
    # Test inconsistent row lengths
    with pytest.raises(ValueError, match="All rows in the matrix must have the same length"):
        find_matrix_coordinates([[1, 2], [3, 4, 5]], 5)

def test_find_matrix_coordinates_empty_elements():
    matrix = [
        [None, 2, 3],
        [4, '', 6],
        [7, 8, 0]
    ]
    assert find_matrix_coordinates(matrix, None) == (0, 0)
    assert find_matrix_coordinates(matrix, '') == (1, 1)
    assert find_matrix_coordinates(matrix, 0) == (2, 2)