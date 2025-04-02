import os
from typing import List, Union

def merge_files(input_files: List[str], output_file: str, separator: str = '\n\n') -> None:
    """
    Merge multiple files into a single output file.

    Args:
        input_files (List[str]): List of paths to input files to be merged.
        output_file (str): Path to the output merged file.
        separator (str, optional): Separator to use between file contents. 
                                   Defaults to double newline.

    Raises:
        FileNotFoundError: If any of the input files do not exist.
        ValueError: If input_files list is empty.
        PermissionError: If there are permission issues reading/writing files.
    """
    # Validate input
    if not input_files:
        raise ValueError("No input files provided.")

    # Check if all input files exist
    for file in input_files:
        if not os.path.exists(file):
            raise FileNotFoundError(f"Input file not found: {file}")

    # Read and merge file contents
    merged_contents = []
    for file in input_files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                merged_contents.append(f.read().strip())
        except (IOError, PermissionError) as e:
            raise PermissionError(f"Error reading file {file}: {e}")

    # Write merged contents to output file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(separator.join(merged_contents))
    except (IOError, PermissionError) as e:
        raise PermissionError(f"Error writing to output file {output_file}: {e}")