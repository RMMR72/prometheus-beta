import os
import bz2

def compress_file(input_path, output_path=None):
    """
    Compress a file using bzip2 compression.

    Args:
        input_path (str): Path to the input file to be compressed.
        output_path (str, optional): Path for the compressed output file. 
                                     If not provided, appends '.bz2' to input path.

    Returns:
        str: Path to the compressed file.

    Raises:
        FileNotFoundError: If the input file does not exist.
        PermissionError: If there are permission issues reading/writing files.
        IsADirectoryError: If input_path is a directory instead of a file.
    """
    # Validate input file exists and is a file
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    if not os.path.isfile(input_path):
        raise IsADirectoryError(f"Input path must be a file, not a directory: {input_path}")

    # Determine output path if not provided
    if output_path is None:
        output_path = input_path + '.bz2'

    # Perform compression
    try:
        with open(input_path, 'rb') as input_file:
            with bz2.open(output_path, 'wb') as compressed_file:
                compressed_file.write(input_file.read())
        
        return output_path
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing files: {input_path} or {output_path}")