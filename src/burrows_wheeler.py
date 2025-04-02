def burrows_wheeler_transform(text):
    """
    Implement the Burrows-Wheeler Transform for data compression.
    
    Args:
        text (str): Input string to be transformed
    
    Returns:
        str: Burrows-Wheeler transformed string
    
    Raises:
        TypeError: If input is not a string
        ValueError: If input is an empty string
    """
    # Input validation
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    if len(text) == 0:
        raise ValueError("Input string cannot be empty")
    
    # Add a special terminator character not in the input
    text_with_terminator = text + '$'
    
    # Generate all rotations of the string
    rotations = [text_with_terminator[i:] + text_with_terminator[:i] 
                 for i in range(len(text_with_terminator))]
    
    # Sort the rotations lexicographically
    sorted_rotations = sorted(rotations)
    
    # Take the last character of each sorted rotation to form the BWT
    bwt = ''.join(rotation[-1] for rotation in sorted_rotations)
    
    return bwt

def inverse_burrows_wheeler_transform(bwt):
    """
    Implement the inverse Burrows-Wheeler Transform to recover the original text.
    
    Args:
        bwt (str): Burrows-Wheeler transformed string
    
    Returns:
        str: Original text before transformation
    
    Raises:
        TypeError: If input is not a string
        ValueError: If input is an empty string
    """
    # Input validation
    if not isinstance(bwt, str):
        raise TypeError("Input must be a string")
    
    if len(bwt) == 0:
        raise ValueError("Input string cannot be empty")
    
    # Prepare first and last columns
    last_column = list(bwt)
    first_column = sorted(last_column)
    
    # Initialize arrays for tracking
    next_char = [0] * len(last_column)
    
    # Compute the last-first mapping
    for i in range(len(last_column)):
        # Find the index of the character in the first column
        char = last_column[i]
        index = first_column.index(char)
        
        # Update tracking
        next_char[i] = index
        
        # Remove the first occurrence of the character to handle duplicates
        first_column.remove(char)
    
    # Reconstruct the original string
    result = []
    current_index = last_column.index('$')  # Start at the terminator
    
    for _ in range(len(last_column) - 1):
        current_index = next_char[current_index]
        result.append(first_column[current_index])
    
    return ''.join(result)