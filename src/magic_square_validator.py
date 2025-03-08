def is_magic_square(numbers):
    """
    Determine if a list of 10 integers represents a valid 3x3 magic square.
    
    A 3x3 magic square has the following properties:
    - Contains exactly 10 integers
    - Uses numbers 1-9 without repetition
    - When arranged in a 3x3 grid, each row, column, and diagonal 
      sum to the same magic constant (15)
    
    Args:
        numbers (list): A list of 10 integers to validate
    
    Returns:
        bool: True if the input forms a valid 3x3 magic square, False otherwise
    
    Raises:
        ValueError: If input is not a list of 10 integers
    """
    # Validate input type and length
    if not isinstance(numbers, list) or len(numbers) != 10:
        return False
    
    # Check if all numbers are integers
    if not all(isinstance(x, int) for x in numbers):
        return False
    
    # Check for unique numbers from 1-9
    unique_nums = set(numbers)
    if len(unique_nums) != 9 or not all(1 <= x <= 9 for x in unique_nums):
        return False
    
    # Create all possible 3x3 arrangements
    def check_square(square):
        # Check rows
        rows = [sum(square[i:i+3]) for i in range(0, 9, 3)]
        # Check columns
        cols = [sum(square[i::3]) for i in range(3)]
        # Check diagonals
        diag1 = sum(square[0::4])  # Top-left to bottom-right
        diag2 = sum(square[2:7:2])  # Top-right to bottom-left
        
        # All lines should sum to 15 (magic constant for 3x3 magic square)
        all_lines = rows + cols + [diag1, diag2]
        return all(line == 15 for line in all_lines)
    
    # Try all permutations of the numbers
    from itertools import permutations
    return any(check_square(list(perm)) for perm in permutations(numbers))