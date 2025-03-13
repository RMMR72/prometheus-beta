def find_longest_consecutive_sequence(numbers):
    """
    Find the longest consecutive sequence of numbers in the input list.

    Args:
        numbers (list): A list of integers to search for consecutive sequences.

    Returns:
        list: The longest consecutive sequence of numbers.
              If multiple sequences have the same length, return the first one.
              Returns an empty list if no consecutive sequence is found.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-integer elements.
    """
    # Validate input
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list
    if not numbers:
        return []
    
    # Validate all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements must be integers")
    
    # Remove duplicates and sort
    unique_nums = sorted(set(numbers))
    
    sequences = []
    current_sequence = [unique_nums[0]]
    
    for i in range(1, len(unique_nums)):
        # Continue or break current sequence
        if unique_nums[i] == unique_nums[i-1] + 1:
            current_sequence.append(unique_nums[i])
        else:
            # Save current sequence
            sequences.append(current_sequence)
            
            # Start a new sequence
            current_sequence = [unique_nums[i]]
    
    # Add the last sequence
    sequences.append(current_sequence)
    
    # Find the longest sequence, preferring sequences that start lower
    longest_sequence = max(sequences, key=lambda seq: (len(seq), -seq[0]))
    
    return longest_sequence