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
    
    # Create a table to track character frequencies
    char_count = {}
    next_occurrence = {}
    
    # First pass: count character frequencies and initialize next_occurrence
    for char in bwt:
        if char not in char_count:
            char_count[char] = 0
            next_occurrence[char] = 0
        char_count[char] += 1
    
    # Sort first and last columns
    first_column = sorted(bwt)
    
    # Create a mapping from indices in the last column to first column
    table = [0] * len(bwt)
    for i, char in enumerate(first_column):
        occurrences = next_occurrence.get(char, 0)
        table[i] = bwt.index(char, occurrences)
        next_occurrence[char] = table[i] + 1
    
    # Reconstruct the original string
    result = []
    current_index = bwt.index('$')
    
    for _ in range(len(bwt) - 1):
        current_index = table[current_index]
        result.append(first_column[current_index])
    
    return ''.join(result)