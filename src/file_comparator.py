"""
Module for comparing files to check if they are identical.

This module provides a function to compare two files and determine 
if their contents are exactly the same.
"""

import os
import hashlib

def are_files_identical(file1_path: str, file2_path: str) -> bool:
    """
    Compare two files to check if they are identical.

    Args:
        file1_path (str): Path to the first file
        file2_path (str): Path to the second file

    Returns:
        bool: True if files are identical, False otherwise

    Raises:
        FileNotFoundError: If either file does not exist
        PermissionError: If there's no read permission for either file
        IsADirectoryError: If either path is a directory
    """
    # Validate file paths
    if not os.path.isfile(file1_path):
        raise FileNotFoundError(f"First file not found: {file1_path}")
    if not os.path.isfile(file2_path):
        raise FileNotFoundError(f"Second file not found: {file2_path}")

    # Check file sizes first (quick initial comparison)
    if os.path.getsize(file1_path) != os.path.getsize(file2_path):
        return False

    # Compare file contents using SHA-256 hash
    def file_hash(filepath):
        """Generate SHA-256 hash for a file."""
        hasher = hashlib.sha256()
        with open(filepath, 'rb') as f:
            # Read file in chunks to handle large files efficiently
            for chunk in iter(lambda: f.read(4096), b''):
                hasher.update(chunk)
        return hasher.hexdigest()

    # Compare file hashes
    return file_hash(file1_path) == file_hash(file2_path)