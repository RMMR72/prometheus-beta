"""
Test suite for file comparison functionality.
"""

import os
import pytest
import tempfile

from src.file_comparator import are_files_identical

def test_identical_files_same_content():
    """Test that identical files return True."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create two files with identical content
        file1_path = os.path.join(tmpdir, 'file1.txt')
        file2_path = os.path.join(tmpdir, 'file2.txt')
        
        with open(file1_path, 'w') as f1, open(file2_path, 'w') as f2:
            test_content = "Hello, world!\nThis is a test."
            f1.write(test_content)
            f2.write(test_content)
        
        assert are_files_identical(file1_path, file2_path) is True

def test_different_files():
    """Test that files with different content return False."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create two files with different content
        file1_path = os.path.join(tmpdir, 'file1.txt')
        file2_path = os.path.join(tmpdir, 'file2.txt')
        
        with open(file1_path, 'w') as f1, open(file2_path, 'w') as f2:
            f1.write("Content 1")
            f2.write("Content 2")
        
        assert are_files_identical(file1_path, file2_path) is False

def test_files_different_lengths():
    """Test files with different lengths return False."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create two files with different lengths
        file1_path = os.path.join(tmpdir, 'file1.txt')
        file2_path = os.path.join(tmpdir, 'file2.txt')
        
        with open(file1_path, 'w') as f1, open(file2_path, 'w') as f2:
            f1.write("Short")
            f2.write("Longer content")
        
        assert are_files_identical(file1_path, file2_path) is False

def test_empty_files():
    """Test that two empty files are identical."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create two empty files
        file1_path = os.path.join(tmpdir, 'file1.txt')
        file2_path = os.path.join(tmpdir, 'file2.txt')
        
        open(file1_path, 'w').close()
        open(file2_path, 'w').close()
        
        assert are_files_identical(file1_path, file2_path) is True

def test_nonexistent_file():
    """Test that FileNotFoundError is raised for nonexistent files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        existing_file = os.path.join(tmpdir, 'existing.txt')
        with open(existing_file, 'w') as f:
            f.write("Content")
        
        nonexistent_file = os.path.join(tmpdir, 'nonexistent.txt')
        
        with pytest.raises(FileNotFoundError):
            are_files_identical(existing_file, nonexistent_file)
        
        with pytest.raises(FileNotFoundError):
            are_files_identical(nonexistent_file, existing_file)

def test_large_files():
    """Test comparison of large files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create two large files with same content
        file1_path = os.path.join(tmpdir, 'large1.txt')
        file2_path = os.path.join(tmpdir, 'large2.txt')
        
        large_content = "A" * (1024 * 1024)  # 1MB of content
        
        with open(file1_path, 'w') as f1, open(file2_path, 'w') as f2:
            f1.write(large_content)
            f2.write(large_content)
        
        assert are_files_identical(file1_path, file2_path) is True

def test_whitespace_sensitive():
    """Test that files with different whitespace are not identical."""
    with tempfile.TemporaryDirectory() as tmpdir:
        file1_path = os.path.join(tmpdir, 'file1.txt')
        file2_path = os.path.join(tmpdir, 'file2.txt')
        
        with open(file1_path, 'w') as f1, open(file2_path, 'w') as f2:
            f1.write("Hello World")
            f2.write("Hello  World")  # Extra space
        
        assert are_files_identical(file1_path, file2_path) is False