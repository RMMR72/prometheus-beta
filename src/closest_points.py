import math
from typing import List, Tuple


def find_closest_points(list_a: List[Tuple[float, float]], 
                        list_b: List[Tuple[float, float]]) -> Tuple[Tuple[Tuple[float, float], Tuple[float, float]], float]:
    """
    Find the two closest points, one from list A and one from list B, 
    based on Euclidean distance.

    Args:
        list_a (List[Tuple[float, float]]): First list of points (x, y coordinates)
        list_b (List[Tuple[float, float]]): Second list of points (x, y coordinates)

    Returns:
        Tuple containing:
        - Tuple of two points (point from A, point from B)
        - Minimum distance between the points

    Raises:
        ValueError: If either input list is empty
    """
    # Validate input
    if not list_a or not list_b:
        raise ValueError("Both input lists must contain at least one point")

    # Initialize minimum distance to a very large value
    min_distance = float('inf')
    closest_points = None

    # Compare each point in list A with each point in list B
    for point_a in list_a:
        for point_b in list_b:
            # Calculate Euclidean distance
            distance = math.sqrt(
                (point_a[0] - point_b[0]) ** 2 + 
                (point_a[1] - point_b[1]) ** 2
            )

            # Update minimum distance if a smaller distance is found
            if distance < min_distance:
                min_distance = distance
                closest_points = (point_a, point_b)

    return closest_points, min_distance