def find_matrix_coordinates(matrix, target):
    """
    Find the coordinates of a target value in a 2D matrix.
    
    Args:
        matrix (List[List[int]]): A 2D matrix to search through
        target (int): The value to find in the matrix
    
    Returns:
        tuple: A tuple of (row, col) coordinates if found, or None if not found
    
    Raises:
        TypeError: If input is not a valid 2D matrix
        ValueError: If matrix is empty
    """
    # Validate input matrix
    if not matrix or not isinstance(matrix, list):
        raise ValueError("Input must be a non-empty matrix")
    
    # Check if matrix is 2D
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("Input must be a 2D matrix")
    
    # Check if all rows have consistent length
    if len(set(len(row) for row in matrix)) > 1:
        raise ValueError("All rows in the matrix must have the same length")
    
    # Search through the matrix
    for row_idx, row in enumerate(matrix):
        for col_idx, value in enumerate(row):
            if value == target:
                return (row_idx, col_idx)
    
    # Return None if target is not found
    return None