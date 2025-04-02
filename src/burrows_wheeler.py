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
    
    # First-last property mapping
    n = len(bwt)
    first_column = sorted(bwt)
    
    # Create a mapping to track character occurrences
    last_count = {}
    first_count = {}
    last_indices = {}
    
    # Prepare occurrence tracking for both last and first columns
    for i, char in enumerate(bwt):
        if char not in last_count:
            last_count[char] = 0
            first_count[char] = 0
            last_indices[char] = []
        
        last_indices[char].append(i)
        last_count[char] += 1
    
    # Reconstruct the original text
    result = []
    current_index = bwt.index('$')
    
    for _ in range(n - 1):
        # Find the corresponding character in the first column
        current_char = bwt[current_index]
        
        # Find next occurrence based on first-last property
        index_in_first = first_column.index(current_char, first_count[current_char])
        
        # Append the character
        result.append(first_column[index_in_first])
        
        # Update counts and move to next index
        first_count[current_char] += 1
        current_index = last_indices[current_char][first_count[current_char] - 1]
    
    return ''.join(result)