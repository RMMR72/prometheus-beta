import os
import pytest
from cryptography.fernet import Fernet
import sys
sys.path.append('src')

from file_encryption import encrypt_file, generate_key

def test_generate_key():
    """Test key generation produces a valid Fernet key."""
    key = generate_key()
    assert isinstance(key, bytes)
    assert len(key) > 0
    # Verify it's a valid Fernet key
    try:
        Fernet(key)
    except Exception as e:
        pytest.fail(f"Generated key is not a valid Fernet key: {e}")

def test_encrypt_file_default(tmp_path):
    """Test encrypting a file with default parameters."""
    # Create a test file
    test_file = tmp_path / "test_input.txt"
    test_file.write_text("Hello, World!")
    
    # Encrypt the file
    key = encrypt_file(str(test_file))
    
    # Verify file was modified
    assert test_file.read_bytes() != b"Hello, World!"
    
    # Verify key was returned
    assert isinstance(key, bytes)
    assert len(key) > 0

def test_encrypt_file_with_custom_key(tmp_path):
    """Test encrypting a file with a custom key."""
    # Create a test file
    test_file = tmp_path / "test_input.txt"
    test_file.write_text("Hello, World!")
    
    # Custom key
    custom_key = generate_key()
    
    # Encrypt the file with custom key
    returned_key = encrypt_file(str(test_file), key=custom_key)
    
    # Verify file was modified
    assert test_file.read_bytes() != b"Hello, World!"
    
    # Verify returned key matches input key
    assert returned_key == custom_key

def test_encrypt_file_to_different_path(tmp_path):
    """Test encrypting a file to a different output path."""
    # Create a test file
    input_file = tmp_path / "test_input.txt"
    input_file.write_text("Hello, World!")
    
    # Output file path
    output_file = tmp_path / "test_output.txt"
    
    # Encrypt the file
    key = encrypt_file(str(input_file), str(output_file))
    
    # Verify input file is unchanged
    assert input_file.read_text() == "Hello, World!"
    
    # Verify output file was created and is different from input
    assert output_file.read_bytes() != b"Hello, World!"
    assert output_file.exists()

def test_encrypt_empty_file(tmp_path):
    """Test that encrypting an empty file raises a ValueError."""
    # Create an empty test file
    test_file = tmp_path / "empty_file.txt"
    test_file.touch()
    
    # Attempt to encrypt should raise ValueError
    with pytest.raises(ValueError, match="Cannot encrypt an empty file"):
        encrypt_file(str(test_file))

def test_encrypt_nonexistent_file():
    """Test that attempting to encrypt a non-existent file raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        encrypt_file("/path/to/nonexistent/file.txt")