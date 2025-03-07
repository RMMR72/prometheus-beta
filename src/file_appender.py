"""
Module for appending text to files.

This module provides a function to safely append text to existing files,
with error handling for various edge cases.
"""

def append_to_file(file_path: str, text: str) -> None:
    """
    Append text to an existing file.

    Args:
        file_path (str): The path to the file to append to.
        text (str): The text to append to the file.

    Raises:
        TypeError: If file_path or text is not a string.
        ValueError: If file_path is an empty string.
        PermissionError: If the file cannot be opened due to permission issues.
        FileNotFoundError: If the file does not exist.
    """
    # Validate input types
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # Validate file path
    if not file_path:
        raise ValueError("file_path cannot be an empty string")
    
    # Append text to the file
    try:
        with open(file_path, 'a') as file:
            file.write(text)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist")
    except PermissionError:
        raise PermissionError(f"Permission denied when trying to append to {file_path}")