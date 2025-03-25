import os
import bz2
import pytest
import tempfile
import shutil

from src.file_compressor import compress_file

def test_compress_file_default_output():
    """Test compression with default output path."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a test file
        test_file_path = os.path.join(tmpdir, 'test_file.txt')
        with open(test_file_path, 'w') as f:
            f.write('Test content for compression')
        
        # Compress the file
        compressed_path = compress_file(test_file_path)
        
        # Verify compressed file exists with .bz2 extension
        assert os.path.exists(compressed_path)
        assert compressed_path == test_file_path + '.bz2'
        
        # Verify file can be decompressed
        with bz2.open(compressed_path, 'rt') as f:
            assert f.read() == 'Test content for compression'

def test_compress_file_custom_output():
    """Test compression with custom output path."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a test file
        test_file_path = os.path.join(tmpdir, 'test_file.txt')
        with open(test_file_path, 'w') as f:
            f.write('Test content for compression')
        
        # Custom output path
        custom_output = os.path.join(tmpdir, 'compressed.bz2')
        compressed_path = compress_file(test_file_path, custom_output)
        
        # Verify compressed file exists at custom path
        assert os.path.exists(compressed_path)
        assert compressed_path == custom_output
        
        # Verify file can be decompressed
        with bz2.open(compressed_path, 'rt') as f:
            assert f.read() == 'Test content for compression'

def test_compress_nonexistent_file():
    """Test that FileNotFoundError is raised for non-existent file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        non_existent_path = os.path.join(tmpdir, 'does_not_exist.txt')
        
        with pytest.raises(FileNotFoundError):
            compress_file(non_existent_path)

def test_compress_directory():
    """Test that IsADirectoryError is raised when input is a directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        with pytest.raises(IsADirectoryError):
            compress_file(tmpdir)

def test_large_file_compression():
    """Test compression of a large file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a large test file
        large_file_path = os.path.join(tmpdir, 'large_file.txt')
        with open(large_file_path, 'w') as f:
            f.write('Test content ' * 10000)  # Create a ~130KB file
        
        # Compress the file
        compressed_path = compress_file(large_file_path)
        
        # Verify compressed file exists and can be decompressed
        assert os.path.exists(compressed_path)
        
        with bz2.open(compressed_path, 'rt') as f:
            assert f.read() == 'Test content ' * 10000