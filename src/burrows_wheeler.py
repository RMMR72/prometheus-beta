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
    
    # First-last column mapping
    n = len(bwt)
    
    # Step 1: Sort the characters of the BWT
    first_column = sorted(bwt)
    
    # Keep track of character indices
    next_index = {char: [i for i, x in enumerate(bwt) if x == char] 
                  for char in set(bwt)}
    indices_used = {char: 0 for char in set(bwt)}
    
    # Reconstruct the original text
    result = []
    current_index = bwt.index('$')
    
    # Reconstruct until we've processed all characters except the terminator
    for _ in range(n - 1):
        # Get the character at the current index in the first column
        current_char = first_column[current_index]
        result.append(current_char)
        
        # Find the next index by looking up the same character 
        # in the order of its occurrence in the last column
        occurrence = indices_used[current_char]
        current_index = next_index[current_char][occurrence]
        indices_used[current_char] += 1
    
    return ''.join(result)