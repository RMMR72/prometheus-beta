"""
LZVN-like Compression Algorithm Implementation

This module provides a simplified compression algorithm 
inspired by run-length and dictionary-based techniques.
"""

def compress_lzvn(data):
    """
    Compress input data using a simplified run-length like algorithm.
    
    Args:
        data (bytes): Input data to be compressed
    
    Returns:
        bytes: Compressed data
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If input is empty
    """
    # Input validation
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes")
    
    if not data:
        raise ValueError("Input data cannot be empty")
    
    compressed = bytearray()
    i = 0
    
    while i < len(data):
        # Find run of identical bytes
        run_length = 1
        while (i + run_length < len(data) and 
               data[i] == data[i + run_length] and 
               run_length < 15):  # 4-bit run length
            run_length += 1
        
        if run_length > 3:
            # Use high 4 bits for run length, low 4 bits for run byte
            compressed_byte = ((run_length & 0x0F) << 4) | (data[i] & 0x0F)
            compressed.append(compressed_byte)
            i += run_length
        else:
            # Literal bytes
            compressed.append(data[i])
            i += 1
    
    return bytes(compressed)

def decompress_lzvn(compressed_data):
    """
    Decompress data compressed with the LZVN-like algorithm.
    
    Args:
        compressed_data (bytes): Input compressed data
    
    Returns:
        bytes: Decompressed original data
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If input is empty or invalid
    """
    # Input validation
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    if not compressed_data:
        raise ValueError("Input data cannot be empty")
    
    decompressed = bytearray()
    i = 0
    
    while i < len(compressed_data):
        current_byte = compressed_data[i]
        
        # Check if this is a run
        if current_byte & 0xF0 != current_byte:
            # High 4 bits represent run length
            run_length = (current_byte & 0xF0) >> 4
            
            # Low 4 bits represent byte to repeat
            run_byte = current_byte & 0x0F
            
            # Expand the run
            for _ in range(run_length):
                decompressed.append(run_byte)
            
            i += 1
        else:
            # Literal byte
            decompressed.append(current_byte)
            i += 1
    
    return bytes(decompressed)