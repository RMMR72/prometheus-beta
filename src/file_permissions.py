import os
import stat

def get_file_permissions(file_path):
    """
    Retrieve the file permissions of a given file.

    Args:
        file_path (str): Path to the file whose permissions are to be retrieved.

    Returns:
        dict: A dictionary containing file permission details:
            - 'numeric': Numeric representation of file permissions (e.g., 0o644)
            - 'readable': Human-readable permission string (e.g., 'rw-r--r--')
            - 'owner_read': Boolean indicating if owner can read
            - 'owner_write': Boolean indicating if owner can write
            - 'owner_execute': Boolean indicating if owner can execute
            - 'group_read': Boolean indicating if group can read
            - 'group_write': Boolean indicating if group can write
            - 'group_execute': Boolean indicating if group can execute
            - 'others_read': Boolean indicating if others can read
            - 'others_write': Boolean indicating if others can write
            - 'others_execute': Boolean indicating if others can execute

    Raises:
        FileNotFoundError: If the specified file does not exist
        PermissionError: If there's no permission to access the file
    """
    try:
        # Get file stats
        file_stat = os.stat(file_path)
        mode = file_stat.st_mode

        # Convert numeric permissions
        numeric_perms = stat.S_IMODE(mode)

        # Create readable permission string
        readable_perms = ''
        readable_perms += 'r' if mode & stat.S_IRUSR else '-'
        readable_perms += 'w' if mode & stat.S_IWUSR else '-'
        readable_perms += 'x' if mode & stat.S_IXUSR else '-'
        readable_perms += 'r' if mode & stat.S_IRGRP else '-'
        readable_perms += 'w' if mode & stat.S_IWGRP else '-'
        readable_perms += 'x' if mode & stat.S_IXGRP else '-'
        readable_perms += 'r' if mode & stat.S_IROTH else '-'
        readable_perms += 'w' if mode & stat.S_IWOTH else '-'
        readable_perms += 'x' if mode & stat.S_IXOTH else '-'

        return {
            'numeric': numeric_perms,
            'readable': readable_perms,
            'owner_read': bool(mode & stat.S_IRUSR),
            'owner_write': bool(mode & stat.S_IWUSR),
            'owner_execute': bool(mode & stat.S_IXUSR),
            'group_read': bool(mode & stat.S_IRGRP),
            'group_write': bool(mode & stat.S_IWGRP),
            'group_execute': bool(mode & stat.S_IXGRP),
            'others_read': bool(mode & stat.S_IROTH),
            'others_write': bool(mode & stat.S_IWOTH),
            'others_execute': bool(mode & stat.S_IXOTH)
        }
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing {file_path}.")