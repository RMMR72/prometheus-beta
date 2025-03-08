def solve_tower_of_hanoi(n, source_rod='A', auxiliary_rod='B', destination_rod='C'):
    """
    Recursively solve the Tower of Hanoi puzzle and print the moves.
    
    Args:
        n (int): Number of disks to move
        source_rod (str): Name of the source rod (default 'A')
        auxiliary_rod (str): Name of the auxiliary rod (default 'B')
        destination_rod (str): Name of the destination rod (default 'C')
    
    Returns:
        list: A list of move tuples representing the sequence of disk moves
    
    Raises:
        ValueError: If the number of disks is negative
    """
    # Validate input
    if n < 0:
        raise ValueError("Number of disks must be non-negative")
    
    # List to store moves
    moves = []
    
    def hanoi_recursive(num_disks, source, auxiliary, destination):
        """
        Internal recursive function to solve Tower of Hanoi
        
        Args:
            num_disks (int): Number of disks to move
            source (str): Source rod
            auxiliary (str): Auxiliary rod
            destination (str): Destination rod
        """
        # Base case: if no disks to move, return
        if num_disks == 0:
            return
        
        # Move n-1 disks from source to auxiliary rod
        hanoi_recursive(num_disks - 1, source, destination, auxiliary)
        
        # Move the nth disk from source to destination
        moves.append((source, destination))
        print(f"Move disk from {source} to {destination}")
        
        # Move n-1 disks from auxiliary to destination rod
        hanoi_recursive(num_disks - 1, auxiliary, source, destination)
    
    # Start the recursive solving process
    hanoi_recursive(n, source_rod, auxiliary_rod, destination_rod)
    
    return moves

# Optional: Add a main block for standalone execution
if __name__ == "__main__":
    solve_tower_of_hanoi(7)  # Solve for 7 disks