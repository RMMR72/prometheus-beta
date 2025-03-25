import os
from typing import Union, Optional

def create_directory(path: str, mode: Optional[int] = 0o755) -> bool:
    """
    Create a new directory with the specified path and optional permissions.

    Args:
        path (str): The path of the directory to create.
        mode (int, optional): The file mode (permissions) for the new directory. 
                               Defaults to 0o755 (rwxr-xr-x).

    Returns:
        bool: True if directory was created successfully, False if directory already exists.

    Raises:
        PermissionError: If the user lacks permission to create the directory.
        OSError: For other OS-related errors during directory creation.
    """
    try:
        # Normalize the path to handle potential relative paths
        normalized_path = os.path.abspath(os.path.expanduser(path))
        
        # Check if directory already exists
        if os.path.exists(normalized_path):
            return False
        
        # Get the parent directory
        parent_dir = os.path.dirname(normalized_path)
        
        # Check parent directory permissions
        if not os.path.exists(parent_dir):
            raise OSError(f"Parent directory does not exist: {parent_dir}")
        
        if not os.access(parent_dir, os.W_OK):
            raise PermissionError(f"No write permission for parent directory: {parent_dir}")
        
        # Create directory with specified mode
        os.makedirs(normalized_path, mode=mode, exist_ok=False)
        return True
    
    except FileExistsError:
        return False