import os
import pathlib

def delete_file(file_path):
    """
    Delete a file from the specified path.

    Args:
        file_path (str): The path to the file to be deleted.

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If the user lacks permission to delete the file.
        IsADirectoryError: If the path points to a directory instead of a file.
        TypeError: If the file_path is not a string.

    Returns:
        bool: True if the file was successfully deleted.
    """
    # Validate input type
    if not isinstance(file_path, (str, pathlib.Path)):
        raise TypeError("File path must be a string or Path object")
    
    # Convert to Path object for consistent handling
    path = pathlib.Path(file_path)
    
    # Check if path exists
    if not path.exists():
        raise FileNotFoundError(f"The file {file_path} does not exist")
    
    # Check if it's a file (not a directory)
    if not path.is_file():
        raise IsADirectoryError(f"{file_path} is a directory, not a file")
    
    try:
        # Delete the file
        path.unlink()
        return True
    except PermissionError:
        raise PermissionError(f"Permission denied: Cannot delete {file_path}")