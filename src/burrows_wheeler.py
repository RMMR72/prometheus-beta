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
    
    # Create sorted list of characters for first column
    first_column = sorted(bwt)
    
    # Create mapping for reconstruction
    mapping = {}
    for i, char in enumerate(bwt):
        if char not in mapping:
            mapping[char] = 0
        mapping[char] += 1
    
    # Build the original text
    reconstructed = [''] * len(bwt)
    next_char_index = bwt.index('$')
    for i in range(len(bwt) - 1, -1, -1):
        reconstructed[i] = bwt[next_char_index]
        
        # Update next_char_index by finding the correct position in the first column
        current_char = bwt[next_char_index]
        count = mapping.get(current_char, 0)
        
        next_char_index = first_column.index(current_char)
        mapping[current_char] -= 1
    
    # Remove the terminator and return
    return ''.join(reconstructed).rstrip('$')