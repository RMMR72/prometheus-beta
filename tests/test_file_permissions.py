import os
import pytest
import stat
from src.file_permissions import get_file_permissions

def test_get_file_permissions_existing_file(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Test content")
    
    # Set specific permissions
    test_file.chmod(0o644)
    
    # Get permissions
    perms = get_file_permissions(str(test_file))
    
    # Verify permissions
    assert perms['numeric'] == 0o644
    assert perms['readable'] == 'rw-r--r--'
    assert perms['owner_read'] == True
    assert perms['owner_write'] == True
    assert perms['owner_execute'] == False
    assert perms['group_read'] == True
    assert perms['group_write'] == False
    assert perms['group_execute'] == False
    assert perms['others_read'] == True
    assert perms['others_write'] == False
    assert perms['others_execute'] == False

def test_get_file_permissions_executable(tmp_path):
    # Create an executable file
    test_file = tmp_path / "test_script.sh"
    test_file.write_text("#!/bin/bash\necho 'Hello'")
    
    # Set executable permissions
    test_file.chmod(0o755)
    
    # Get permissions
    perms = get_file_permissions(str(test_file))
    
    # Verify permissions
    assert perms['numeric'] == 0o755
    assert perms['readable'] == 'rwxr-xr-x'
    assert perms['owner_execute'] == True
    assert perms['group_execute'] == True
    assert perms['others_execute'] == True

def test_get_file_permissions_no_permissions(tmp_path):
    # Create a file with no permissions
    test_file = tmp_path / "no_perm_file.txt"
    test_file.write_text("No permissions")
    
    # Set no permissions
    test_file.chmod(0o000)
    
    # Get permissions
    perms = get_file_permissions(str(test_file))
    
    # Verify permissions
    assert perms['numeric'] == 0o000
    assert perms['readable'] == '---------'
    assert perms['owner_read'] == False
    assert perms['owner_write'] == False
    assert perms['owner_execute'] == False
    assert perms['group_read'] == False
    assert perms['others_write'] == False

def test_get_file_permissions_nonexistent_file():
    # Test for non-existent file
    with pytest.raises(FileNotFoundError):
        get_file_permissions("/path/to/nonexistent/file.txt")

def test_get_file_permissions_inaccessible_file(tmp_path):
    # Create a file that might be inaccessible
    test_file = tmp_path / "inaccessible_file.txt"
    test_file.write_text("Inaccessible content")
    
    # Remove read permissions
    test_file.chmod(0o000)
    
    # Try to read permissions, should raise PermissionError
    with pytest.raises(PermissionError):
        get_file_permissions(str(test_file))