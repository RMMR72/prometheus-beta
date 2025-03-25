from typing import List, Tuple

def cleanRoom(grid: List[List[int]], r: int, c: int, direction: str) -> int:
    """
    Calculate the minimum number of steps required to clean an entire grid-based room.
    
    Args:
        grid (List[List[int]]): 2D grid representing the room layout
            0 represents an empty cell that can be cleaned
            1 represents an obstacle that cannot be cleaned
        r (int): Starting row position of the robot
        c (int): Starting column position of the robot
        direction (str): Initial direction of the robot ('N', 'S', 'E', 'W')
    
    Returns:
        int: Minimum number of steps required to clean the entire room
        
    Raises:
        ValueError: If the input grid is invalid or starting position is out of bounds
    """
    # Validate input
    if not grid or not grid[0]:
        raise ValueError("Grid cannot be empty")
    
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        raise ValueError("Starting position is out of grid bounds")
    
    # Check if there are any cleanable cells
    cleanable_cells = sum(row.count(0) for row in grid)
    if cleanable_cells == 0:
        raise ValueError("No cleanable cells in the grid")
    
    # Directions: North, East, South, West
    directions = ['N', 'E', 'S', 'W']
    
    # Possible moves in order: North, East, South, West
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    def is_valid_move(x: int, y: int) -> bool:
        """Check if the move is within grid bounds and not an obstacle."""
        return (0 <= x < len(grid) and 
                0 <= y < len(grid[0]) and 
                grid[x][y] == 0)
    
    # Track visited cells
    visited = set()
    
    def backtrack(x: int, y: int, curr_dir_idx: int) -> int:
        """
        Recursive backtracking to clean the room
        
        Args:
            x (int): Current row
            y (int): Current column
            curr_dir_idx (int): Current direction index
        
        Returns:
            int: Number of steps to explore the room
        """
        # Mark current cell as visited
        visited.add((x, y))
        
        total_steps = 0
        # Try moving in each direction
        for i in range(4):
            # New direction (rotating clockwise)
            new_dir_idx = (curr_dir_idx + i) % 4
            dx, dy = moves[new_dir_idx]
            new_x, new_y = x + dx, y + dy
            
            # If move is valid and not visited
            if is_valid_move(new_x, new_y) and (new_x, new_y) not in visited:
                total_steps += 1  # Count the step
                total_steps += backtrack(new_x, new_y, new_dir_idx)
        
        return total_steps
    
    # Start direction index
    start_dir_idx = directions.index(direction)
    
    # Start cleaning and explore the room
    result = backtrack(r, c, start_dir_idx)
    
    return result