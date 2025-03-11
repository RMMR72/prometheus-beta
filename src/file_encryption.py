from cryptography.fernet import Fernet
import os

def generate_key():
    """
    Generate a new encryption key.
    
    Returns:
        bytes: A new encryption key.
    """
    return Fernet.generate_key()

def encrypt_file(input_path, output_path=None, key=None):
    """
    Encrypt the contents of a file.
    
    Args:
        input_path (str): Path to the input file to be encrypted.
        output_path (str, optional): Path to save the encrypted file. 
                                     If not provided, overwrites input file.
        key (bytes, optional): Encryption key. If not provided, a new key is generated.
    
    Returns:
        bytes: The encryption key used.
    
    Raises:
        FileNotFoundError: If input file does not exist.
        PermissionError: If there are permission issues reading/writing files.
        ValueError: If input file is empty.
    """
    # Validate input path
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # Check file is not empty
    if os.path.getsize(input_path) == 0:
        raise ValueError("Cannot encrypt an empty file")
    
    # Use provided key or generate new
    if key is None:
        key = generate_key()
    
    # Create Fernet cipher
    fernet = Fernet(key)
    
    # Read input file
    try:
        with open(input_path, 'rb') as file:
            file_data = file.read()
    except PermissionError:
        raise PermissionError(f"Permission denied reading file: {input_path}")
    
    # Encrypt file contents
    encrypted_data = fernet.encrypt(file_data)
    
    # Determine output path
    if output_path is None:
        output_path = input_path
    
    # Write encrypted data
    try:
        with open(output_path, 'wb') as file:
            file.write(encrypted_data)
    except PermissionError:
        raise PermissionError(f"Permission denied writing to file: {output_path}")
    
    return key