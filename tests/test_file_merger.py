import os
import pytest
import tempfile

from src.file_merger import merge_files

def test_merge_files_basic():
    """Test basic file merging functionality."""
    # Create temporary files
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create input files
        file1 = os.path.join(tmpdir, 'file1.txt')
        file2 = os.path.join(tmpdir, 'file2.txt')
        output = os.path.join(tmpdir, 'merged.txt')
        
        with open(file1, 'w') as f1:
            f1.write("Hello")
        with open(file2, 'w') as f2:
            f2.write("World")
        
        # Merge files
        merge_files([file1, file2], output)
        
        # Check merged content
        with open(output, 'r') as f:
            content = f.read()
            assert content == "Hello\n\nWorld"

def test_merge_files_custom_separator():
    """Test merging with a custom separator."""
    with tempfile.TemporaryDirectory() as tmpdir:
        file1 = os.path.join(tmpdir, 'file1.txt')
        file2 = os.path.join(tmpdir, 'file2.txt')
        output = os.path.join(tmpdir, 'merged.txt')
        
        with open(file1, 'w') as f1:
            f1.write("Hello")
        with open(file2, 'w') as f2:
            f2.write("World")
        
        # Merge files with custom separator
        merge_files([file1, file2], output, separator=' | ')
        
        # Check merged content
        with open(output, 'r') as f:
            content = f.read()
            assert content == "Hello | World"

def test_merge_files_empty_list():
    """Test that merging with an empty list raises ValueError."""
    with tempfile.TemporaryDirectory() as tmpdir:
        output = os.path.join(tmpdir, 'merged.txt')
        
        with pytest.raises(ValueError, match="No input files provided"):
            merge_files([], output)

def test_merge_files_nonexistent_file():
    """Test that trying to merge a nonexistent file raises FileNotFoundError."""
    with tempfile.TemporaryDirectory() as tmpdir:
        output = os.path.join(tmpdir, 'merged.txt')
        nonexistent_file = os.path.join(tmpdir, 'nonexistent.txt')
        
        with pytest.raises(FileNotFoundError, match="Input file not found"):
            merge_files([nonexistent_file], output)

def test_merge_files_single_file():
    """Test merging a single file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        file1 = os.path.join(tmpdir, 'file1.txt')
        output = os.path.join(tmpdir, 'merged.txt')
        
        with open(file1, 'w') as f1:
            f1.write("Single file content")
        
        # Merge single file
        merge_files([file1], output)
        
        # Check merged content
        with open(output, 'r') as f:
            content = f.read()
            assert content == "Single file content"