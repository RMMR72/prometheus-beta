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
    
    longest_sequence = []
    current_sequence = []
    
    for i in range(len(unique_nums)):
        # Start a new sequence or continue current sequence
        if not current_sequence or unique_nums[i] == current_sequence[-1] + 1:
            current_sequence.append(unique_nums[i])
        else:
            # Update longest sequence if current is longer
            if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence
            
            # Reset current sequence
            current_sequence = [unique_nums[i]]
    
    # Check one last time after the loop
    if len(current_sequence) > len(longest_sequence):
        longest_sequence = current_sequence
    
    return longest_sequence