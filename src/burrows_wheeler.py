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
    
    # Prepare first and last columns
    last_column = list(bwt)
    first_column = sorted(last_column)
    
    # Create a table that maps each character in the last column
    # to its corresponding character in the first column
    n = len(last_column)
    occurrence_count = {}
    next_mapping = [0] * n
    
    # Create mapping
    for i in range(n):
        char = last_column[i]
        
        # Calculate the occurrence of this character in first_column
        if char not in occurrence_count:
            occurrence_count[char] = 0
        current_occurrence = occurrence_count[char]
        
        # Find the index of this occurrence in the first_column
        current_index = first_column.index(char, current_occurrence)
        
        # Map last column index to first column index
        next_mapping[i] = current_index
        
        # Update occurrence count
        occurrence_count[char] += 1
    
    # Reconstruct the original string
    result = []
    current_index = last_column.index('$')
    
    # Skip the terminator
    for _ in range(n - 1):
        current_index = next_mapping[current_index]
        result.append(first_column[current_index])
    
    return ''.join(result)