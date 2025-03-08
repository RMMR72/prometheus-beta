def check_letter_case_balance(input_string: str) -> str:
    """
    Check if a given string contains an equal number of uppercase and lowercase letters.

    Args:
        input_string (str): The input string to check for letter case balance.

    Returns:
        str: 'Balanced' if the string has an equal number of uppercase and lowercase letters,
             'Not Balanced' otherwise.

    Raises:
        ValueError: If the input string contains no letters.
    """
    # Count uppercase and lowercase letters
    uppercase_count = sum(1 for char in input_string if char.isupper())
    lowercase_count = sum(1 for char in input_string if char.islower())

    # Check if there are no letters in the string
    if uppercase_count + lowercase_count == 0:
        raise ValueError("Input string must contain at least one letter")

    # Return 'Balanced' if counts are equal, 'Not Balanced' otherwise
    return 'Balanced' if uppercase_count == lowercase_count else 'Not Balanced'