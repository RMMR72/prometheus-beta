import os
import pathlib
import pytest
import tempfile

from src.file_deletion import delete_file

def test_delete_existing_file():
    """Test deleting an existing file."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    # Ensure file exists before deletion
    assert os.path.exists(temp_path)
    
    # Delete the file
    result = delete_file(temp_path)
    
    # Verify deletion
    assert result is True
    assert not os.path.exists(temp_path)

def test_delete_nonexistent_file():
    """Test that deleting a non-existent file raises FileNotFoundError."""
    non_existent_path = "/tmp/definitely_not_existing_file_12345.txt"
    
    with pytest.raises(FileNotFoundError):
        delete_file(non_existent_path)

def test_delete_directory():
    """Test that attempting to delete a directory raises IsADirectoryError."""
    with tempfile.TemporaryDirectory() as temp_dir:
        with pytest.raises(IsADirectoryError):
            delete_file(temp_dir)

def test_delete_invalid_input_type():
    """Test that invalid input types raise TypeError."""
    with pytest.raises(TypeError):
        delete_file(12345)
    
    with pytest.raises(TypeError):
        delete_file(None)

def test_pathlib_input():
    """Test that the function works with pathlib.Path input."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = pathlib.Path(temp_file.name)
    
    # Ensure file exists before deletion
    assert temp_path.exists()
    
    # Delete the file using pathlib.Path
    result = delete_file(temp_path)
    
    # Verify deletion
    assert result is True
    assert not temp_path.exists()