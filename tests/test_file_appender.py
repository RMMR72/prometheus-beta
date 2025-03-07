"""
Tests for the file_appender module.

This test suite covers various scenarios for the append_to_file function.
"""

import os
import pytest
import tempfile

from src.file_appender import append_to_file

def test_append_to_file_basic():
    """Test basic functionality of appending text to a file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Initial content\n")
        temp_file.close()
        
        try:
            append_to_file(temp_file.name, "Additional text\n")
            
            with open(temp_file.name, 'r') as f:
                content = f.read()
                assert content == "Initial content\nAdditional text\n"
        finally:
            os.unlink(temp_file.name)

def test_append_to_file_empty_file():
    """Test appending to an empty file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.close()
        
        try:
            append_to_file(temp_file.name, "Text to append\n")
            
            with open(temp_file.name, 'r') as f:
                content = f.read()
                assert content == "Text to append\n"
        finally:
            os.unlink(temp_file.name)

def test_append_multiple_times():
    """Test appending multiple times to the same file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.close()
        
        try:
            append_to_file(temp_file.name, "First line\n")
            append_to_file(temp_file.name, "Second line\n")
            
            with open(temp_file.name, 'r') as f:
                content = f.read()
                assert content == "First line\nSecond line\n"
        finally:
            os.unlink(temp_file.name)

def test_invalid_file_path_type():
    """Test passing non-string file path raises TypeError."""
    with pytest.raises(TypeError, match="file_path must be a string"):
        append_to_file(123, "text")

def test_invalid_text_type():
    """Test passing non-string text raises TypeError."""
    with pytest.raises(TypeError, match="text must be a string"):
        append_to_file("file.txt", 123)

def test_empty_file_path():
    """Test passing an empty file path raises ValueError."""
    with pytest.raises(ValueError, match="file_path cannot be an empty string"):
        append_to_file("", "text")

def test_nonexistent_file():
    """Test attempting to append to a nonexistent file raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        append_to_file("nonexistent_directory/nonexistent_file.txt", "text")

# Note: Testing PermissionError would require special setup and might 
# not be consistently reproducible across different systems.