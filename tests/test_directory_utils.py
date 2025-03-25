import os
import pytest
import tempfile
import sys

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from directory_utils import create_directory

def test_create_directory_success():
    """Test successful directory creation"""
    with tempfile.TemporaryDirectory() as temp_base:
        test_dir = os.path.join(temp_base, 'new_directory')
        result = create_directory(test_dir)
        assert result is True
        assert os.path.exists(test_dir)
        assert os.path.isdir(test_dir)

def test_create_directory_already_exists():
    """Test attempting to create an existing directory"""
    with tempfile.TemporaryDirectory() as temp_base:
        test_dir = os.path.join(temp_base, 'existing_directory')
        os.makedirs(test_dir)
        
        result = create_directory(test_dir)
        assert result is False
        assert os.path.exists(test_dir)

def test_create_nested_directory():
    """Test creating nested directories"""
    with tempfile.TemporaryDirectory() as temp_base:
        test_dir = os.path.join(temp_base, 'parent', 'child', 'grandchild')
        result = create_directory(test_dir)
        assert result is True
        assert os.path.exists(test_dir)
        assert os.path.isdir(test_dir)

def test_create_directory_permissions():
    """Test directory creation with specific permissions"""
    with tempfile.TemporaryDirectory() as temp_base:
        test_dir = os.path.join(temp_base, 'permissions_dir')
        result = create_directory(test_dir, mode=0o700)
        assert result is True
        
        # Check directory permissions (Unix-like systems only)
        if hasattr(os, 'stat'):
            mode = os.stat(test_dir).st_mode
            assert (mode & 0o777) == 0o700