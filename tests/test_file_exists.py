import os
import pytest
import tempfile

from src.file_exists import is_file_exists

def test_existing_file():
    """Test that an existing file returns True."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file_path = temp_file.name
    
    try:
        assert is_file_exists(temp_file_path) is True
    finally:
        # Clean up the temporary file
        os.unlink(temp_file_path)

def test_non_existing_file():
    """Test that a non-existing file returns False."""
    non_existent_path = "/path/to/definitely/non/existing/file.txt"
    assert is_file_exists(non_existent_path) is False

def test_directory():
    """Test that a directory returns False."""
    with tempfile.TemporaryDirectory() as temp_dir:
        assert is_file_exists(temp_dir) is False

def test_invalid_input_type():
    """Test that non-string inputs raise a TypeError."""
    with pytest.raises(TypeError, match="File path must be a string"):
        is_file_exists(123)
    
    with pytest.raises(TypeError, match="File path must be a string"):
        is_file_exists(None)

def test_empty_string():
    """Test an empty string path."""
    assert is_file_exists("") is False

def test_relative_path():
    """Test that relative paths work correctly."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file_path = temp_file.name
        relative_path = os.path.relpath(temp_file_path)
    
    try:
        assert is_file_exists(relative_path) is True
    finally:
        # Clean up the temporary file
        os.unlink(temp_file_path)