import zlib
from typing import Union, Optional

def compress_data(data: Union[str, bytes], 
                  compression_level: int = 6, 
                  encoding: str = 'utf-8') -> bytes:
    """
    Compress data using Zlib compression algorithm.

    Args:
        data (Union[str, bytes]): The data to compress. 
                                  Can be a string or bytes object.
        compression_level (int, optional): Compression level from 0-9. 
                                           Defaults to 6 (default zlib compression).
                                           0 = no compression, 9 = max compression
        encoding (str, optional): Encoding to use if input is a string. 
                                  Defaults to 'utf-8'.

    Returns:
        bytes: Compressed data as a bytes object.

    Raises:
        ValueError: If compression level is not between 0 and 9
        TypeError: If input data is not a string or bytes object
    """
    # Validate compression level
    if compression_level < 0 or compression_level > 9:
        raise ValueError("Compression level must be between 0 and 9")

    # Convert string to bytes if necessary
    if isinstance(data, str):
        data = data.encode(encoding)
    
    # Validate input type
    if not isinstance(data, bytes):
        raise TypeError("Input must be a string or bytes object")

    # Compress the data
    try:
        compressed_data = zlib.compress(data, compression_level)
        return compressed_data
    except Exception as e:
        raise RuntimeError(f"Compression failed: {str(e)}")

def decompress_data(compressed_data: bytes, 
                    encoding: Optional[str] = 'utf-8') -> Union[bytes, str]:
    """
    Decompress Zlib compressed data.

    Args:
        compressed_data (bytes): The compressed data to decompress.
        encoding (str, optional): Encoding to use for converting 
                                  bytes to string. If None, returns bytes.
                                  Defaults to 'utf-8'.

    Returns:
        Union[bytes, str]: Decompressed data as bytes or string.

    Raises:
        TypeError: If input is not a bytes object
        zlib.error: If decompression fails
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be a bytes object")

    # Decompress the data
    try:
        decompressed_data = zlib.decompress(compressed_data)
        
        # Convert to string if encoding is provided
        if encoding is not None:
            return decompressed_data.decode(encoding)
        return decompressed_data
    except zlib.error as e:
        raise zlib.error(f"Decompression failed: {str(e)}")