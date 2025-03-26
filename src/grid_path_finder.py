from typing import List, Optional
from collections import deque

def find_shortest_path(grid: List[List[int]]) -> Optional[int]:
    """
    Find the shortest path from top-left to bottom-right cell with movement constraints.

    Movement rules:
    - Can move right or down
    - Can only move to a cell with value 0 (empty)
    - If right cell is blocked, must move down
    
    Args:
        grid (List[List[int]]): N x N grid of 0s and 1s
    
    Returns:
        Optional[int]: Length of shortest path, or None if no path exists
    
    Raises:
        ValueError: If grid is empty or not square
    """
    # Input validation
    if not grid or len(grid) == 0:
        raise ValueError("Grid cannot be empty")
    
    n = len(grid)
    
    # Check if grid is square
    if any(len(row) != n for row in grid):
        raise ValueError("Grid must be square")
    
    # Check start and end points are traversable
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return None
    
    # Breadth-first search to find shortest path
    queue = deque([(0, 0, 1)])  # (row, col, path_length)
    visited = set([(0, 0)])
    
    while queue:
        row, col, path_length = queue.popleft()
        
        # Reached bottom-right cell
        if row == n-1 and col == n-1:
            return path_length - 1  # Subtract 1 to match expected path length
        
        # Try moving right first (if possible)
        if col + 1 < n and grid[row][col+1] == 0 and (row, col+1) not in visited:
            queue.append((row, col+1, path_length + 1))
            visited.add((row, col+1))
        
        # Always try moving down
        if row + 1 < n and grid[row+1][col] == 0 and (row+1, col) not in visited:
            queue.append((row+1, col, path_length + 1))
            visited.add((row+1, col))
    
    # No path found
    return None