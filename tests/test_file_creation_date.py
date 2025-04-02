import os
import pytest
from datetime import datetime, timedelta
import time

from src.file_creation_date import get_file_creation_date

def test_get_file_creation_date_existing_file(tmp_path):
    """Test getting creation date for an existing file."""
    # Create a test file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Test content")
    
    # Get creation date
    creation_date = get_file_creation_date(str(test_file))
    
    # Check if creation date is a datetime object and is very recent
    assert isinstance(creation_date, datetime)
    assert datetime.now() - creation_date < timedelta(seconds=5)

def test_get_file_creation_date_nonexistent_file():
    """Test that FileNotFoundError is raised for non-existent file."""
    with pytest.raises(FileNotFoundError):
        get_file_creation_date("non_existent_file.txt")

def test_get_file_creation_date_multiple_files(tmp_path):
    """Test that creation dates are different for multiple files."""
    # Create first file
    first_file = tmp_path / "first_file.txt"
    first_file.write_text("First content")
    time.sleep(0.1)  # Ensure time difference
    
    # Create second file
    second_file = tmp_path / "second_file.txt"
    second_file.write_text("Second content")
    
    # Get creation dates
    first_creation_date = get_file_creation_date(str(first_file))
    second_creation_date = get_file_creation_date(str(second_file))
    
    # Ensure creation dates are different
    assert first_creation_date != second_creation_date