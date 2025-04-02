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
    
    # Special case for single character + terminator
    if len(bwt) == 2 and '$' in bwt:
        return bwt[0]
    
    # First-Last Property: build first column from sorted last column
    n = len(bwt)
    first_column = sorted(bwt)
    
    # Create mapping from last column to first column
    # This helps us reconstruct the original text
    # We'll use counting to handle repeated characters
    last_column_indices = {}
    next_indices = [0] * n
    
    for i, char in enumerate(bwt):
        if char not in last_column_indices:
            last_column_indices[char] = 0
        
        # Find the index of this character in first column
        current_count = last_column_indices[char]
        current_index = first_column.index(char, current_count)
        
        next_indices[i] = current_index
        last_column_indices[char] += 1
    
    # Reconstruct the original text
    result = []
    current_index = bwt.index('$')
    
    # Skip the terminator
    for _ in range(n - 1):
        current_index = next_indices[current_index]
        result.append(first_column[current_index])
    
    return ''.join(result)