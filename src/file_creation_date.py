import os
from datetime import datetime

def get_file_creation_date(file_path):
    """
    Get the creation date of a file.

    Args:
        file_path (str): Path to the file.

    Returns:
        datetime: The creation date of the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        OSError: If there is an error accessing the file metadata.
    """
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        # Get file creation time using platform-specific method
        # On Unix-like systems (Linux, macOS), this uses file metadata creation time
        # On Windows, this uses the actual file creation time
        creation_timestamp = os.path.getctime(file_path)
        
        # Convert timestamp to datetime object
        return datetime.fromtimestamp(creation_timestamp)
    except Exception as e:
        raise OSError(f"Error accessing file metadata: {e}")