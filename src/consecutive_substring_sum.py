def max_consecutive_substring_sum(input_string):
    """
    Calculate the maximum sum of consecutive characters that are also consecutive in the input string.
    
    Args:
        input_string (str): The input string to analyze.
    
    Returns:
        int: The maximum sum of consecutive characters.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input string is empty.
    """
    # Validate input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    # Convert string characters to their ASCII/Unicode values
    char_values = [ord(char.lower()) for char in input_string]
    
    # Initialize variables for Kadane's algorithm variant
    max_sum = char_values[0]
    current_sum = char_values[0]
    
    for i in range(1, len(char_values)):
        # Check if current character is consecutive with previous character
        if char_values[i] == char_values[i-1] + 1:
            current_sum += char_values[i]
        else:
            # Reset current sum if sequence breaks
            current_sum = char_values[i]
        
        # Update max sum if current sum is larger
        max_sum = max(max_sum, current_sum)
    
    return max_sum