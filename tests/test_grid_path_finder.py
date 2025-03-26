import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from grid_path_finder import find_shortest_path

def test_basic_traversable_grid():
    """Test a simple grid where a path exists"""
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert find_shortest_path(grid) == 4

def test_no_path_exists():
    """Test when no path can be found"""
    grid = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ]
    assert find_shortest_path(grid) is None

def test_blocked_start_or_end():
    """Test when start or end is blocked"""
    # Blocked start
    grid1 = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert find_shortest_path(grid1) is None
    
    # Blocked end
    grid2 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]
    assert find_shortest_path(grid2) is None

def test_larger_grid():
    """Test a larger grid with a more complex path"""
    grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]
    assert find_shortest_path(grid) == 7

def test_invalid_input():
    """Test invalid input scenarios"""
    # Empty grid
    with pytest.raises(ValueError):
        find_shortest_path([])
    
    # Non-square grid
    with pytest.raises(ValueError):
        find_shortest_path([
            [0, 0, 0],
            [0, 0]
        ])

def test_single_cell_grid():
    """Test a single cell grid"""
    grid = [[0]]
    assert find_shortest_path(grid) == 1