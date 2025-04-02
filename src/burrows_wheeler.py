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
    
    # Create first column by sorting last column
    n = len(bwt)
    first_column = sorted(bwt)
    
    # Compute the last-to-first column mapping
    next_indices = [0] * n
    char_count = {}
    
    for i in range(n):
        char = bwt[i]
        if char not in char_count:
            char_count[char] = 0
        
        # Find the first occurrence of this character in the first column
        next_index = first_column.index(char, char_count[char])
        next_indices[i] = next_index
        
        # Increment the count for this character
        char_count[char] += 1
    
    # Reconstruct the text, working backwards from the terminator
    result = []
    current_index = bwt.index('$')
    
    for _ in range(n - 1):
        current_index = next_indices[current_index]
        result.append(first_column[current_index])
    
    return ''.join(result)