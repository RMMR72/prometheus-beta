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
    
    # Sort the last column to get the first column
    first_column = sorted(bwt)
    
    # Create a mapping from characters in the last column to their first column indices
    n = len(bwt)
    
    # Count the occurrences of each character
    char_counts = {}
    
    # Will store the indices in the first column where each character appears
    first_occurrence = {}
    
    # Create the mapping
    for i, char in enumerate(first_column):
        # Count occurrences to handle repeated characters
        if char not in char_counts:
            char_counts[char] = 0
            first_occurrence[char] = i
        char_counts[char] += 1
    
    # Reset character counts for last column
    char_counts = {char: 0 for char in first_column}
    
    # Reconstruct the original string
    result = []
    current_index = bwt.index('$')
    
    for _ in range(n - 1):
        # Follow the last-first mapping
        current_char = bwt[current_index]
        
        # Find the corresponding index in the first column
        count = char_counts.get(current_char, 0)
        next_index = first_occurrence[current_char] + count
        
        # Add the character
        result.append(first_column[next_index])
        
        # Update the count for this character
        char_counts[current_char] = count + 1
        
        # Update the current index to the next character in the last column
        current_index = next_index
    
    return ''.join(result)