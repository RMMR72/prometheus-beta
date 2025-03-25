import pytest
from src.robot_vacuum import cleanRoom

def test_basic_empty_room():
    """Test cleaning a simple empty room"""
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    steps = cleanRoom(grid, 1, 1, 'N')
    assert steps == 8  # Should visit all cells

def test_room_with_obstacles():
    """Test cleaning a room with obstacles"""
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    steps = cleanRoom(grid, 0, 0, 'E')
    assert steps >= 6  # At least 6 steps, allowing for different paths
    assert steps <= 8  # But not too many

def test_single_cell_room():
    """Test a single cell room"""
    grid = [[0]]
    steps = cleanRoom(grid, 0, 0, 'N')
    assert steps == 0  # No additional steps needed

def test_room_with_no_cleanable_cells():
    """Test a room with all obstacles"""
    grid = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    with pytest.raises(ValueError):
        cleanRoom(grid, 0, 0, 'N')

def test_invalid_starting_position():
    """Test invalid starting position"""
    grid = [
        [0, 0, 0],
        [0, 0, 0]
    ]
    with pytest.raises(ValueError):
        cleanRoom(grid, 2, 2, 'N')

def test_empty_grid():
    """Test empty grid"""
    with pytest.raises(ValueError):
        cleanRoom([], 0, 0, 'N')

def test_different_directions():
    """Test cleaning with different starting directions"""
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    steps_north = cleanRoom(grid, 1, 1, 'N')
    steps_east = cleanRoom(grid, 1, 1, 'E')
    steps_south = cleanRoom(grid, 1, 1, 'S')
    steps_west = cleanRoom(grid, 1, 1, 'W')
    
    assert steps_north == 8
    assert steps_east == 8
    assert steps_south == 8
    assert steps_west == 8