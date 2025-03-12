"""
LZVN Compression Algorithm Implementation

This module provides a basic implementation of the LZVN (LZ Variant New) 
compression algorithm. The implementation focuses on core compression 
and decompression mechanisms.

Note: This is a simplified version and may not capture all nuances of 
the full LZVN algorithm used in Apple's systems.
"""

def compress_lzvn(data):
    """
    Compress input data using a basic LZVN-like compression algorithm.
    
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
        # Look-ahead window for finding repeated sequences
        match_length = 0
        match_offset = 0
        
        # Search back for potential matches
        for j in range(max(0, i - 4096), i):
            current_match_length = 0
            
            # Check for sequence match
            while (i + current_match_length < len(data) and 
                   data[j + current_match_length] == data[i + current_match_length] and 
                   current_match_length < 32):  # Limit match length
                current_match_length += 1
            
            # Update best match
            if current_match_length > match_length:
                match_length = current_match_length
                match_offset = i - j
        
        # Encode based on match
        if match_length > 2:
            # Compressed sequence: use offset and length encoding
            compressed.append(match_length | ((match_offset & 0x0F) << 5))
            compressed.append(match_offset >> 4)
            i += match_length
        else:
            # Literal byte
            compressed.append(data[i])
            i += 1
    
    return bytes(compressed)

def decompress_lzvn(compressed_data):
    """
    Decompress LZVN-like compressed data.
    
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
        # Check for compressed sequence or literal
        first_byte = compressed_data[i]
        
        # Check if this is a compressed sequence
        if first_byte & 0x1F != first_byte:
            match_length = first_byte & 0x1F
            
            if i + 1 >= len(compressed_data):
                raise ValueError("Invalid compressed data")
            
            offset_high = compressed_data[i + 1]
            match_offset = ((first_byte & 0xE0) >> 5) | (offset_high << 4)
            
            # Reconstruct matching sequence
            start = len(decompressed) - match_offset
            for j in range(match_length):
                decompressed.append(decompressed[start + j])
            
            i += 2
        else:
            # Literal byte
            decompressed.append(first_byte)
            i += 1
    
    return bytes(decompressed)