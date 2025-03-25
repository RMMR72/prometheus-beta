import pytest
import math
from src.closest_points import find_closest_points


def test_find_closest_points_basic():
    """Test basic functionality with simple point lists"""
    list_a = [(0, 0), (1, 1), (3, 4)]
    list_b = [(2, 2), (5, 5), (0, 5)]
    
    result, distance = find_closest_points(list_a, list_b)
    
    # Verify result is a tuple of two points
    assert len(result) == 2
    assert len(result[0]) == 2 and len(result[1]) == 2
    
    # Verify distance is correct
    expected_distance = math.sqrt((1 - 2)**2 + (1 - 2)**2)
    assert math.isclose(distance, expected_distance, rel_tol=1e-9)


def test_find_closest_points_same_list():
    """Test points very close to each other"""
    list_a = [(0, 0), (0.1, 0.1), (2, 2)]
    list_b = [(0.2, 0.2), (3, 3), (4, 4)]
    
    result, distance = find_closest_points(list_a, list_b)
    
    # Verify result is a tuple of two points
    assert len(result) == 2
    assert len(result[0]) == 2 and len(result[1]) == 2
    
    # Verify distance is correct
    expected_distance = math.sqrt((0.1 - 0.2)**2 + (0.1 - 0.2)**2)
    assert math.isclose(distance, expected_distance, rel_tol=1e-9)


def test_find_closest_points_large_coordinates():
    """Test with large coordinate values"""
    list_a = [(1000, 2000), (1500, 2500), (2000, 3000)]
    list_b = [(1100, 2100), (1600, 2600), (2100, 3100)]
    
    result, distance = find_closest_points(list_a, list_b)
    
    # Verify result is a tuple of two points
    assert len(result) == 2
    assert len(result[0]) == 2 and len(result[1]) == 2
    
    # Verify distance calculation
    closest_distance = min(
        math.sqrt((1000 - 1100)**2 + (2000 - 2100)**2),
        math.sqrt((1500 - 1600)**2 + (2500 - 2600)**2),
        math.sqrt((2000 - 2100)**2 + (3000 - 3100)**2)
    )
    assert math.isclose(distance, closest_distance, rel_tol=1e-9)


def test_find_closest_points_empty_list_error():
    """Test that an error is raised when either list is empty"""
    with pytest.raises(ValueError, match="Both input lists must contain at least one point"):
        find_closest_points([], [(1, 2)])
    
    with pytest.raises(ValueError, match="Both input lists must contain at least one point"):
        find_closest_points([(1, 2)], [])