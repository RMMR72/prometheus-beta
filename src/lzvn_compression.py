"""
LZVN Compression Algorithm Implementation

This module provides a basic implementation of the LZVN-like 
compression and decompression algorithms.
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
        # Look for potential repeats
        best_match_length = 0
        best_match_offset = 0
        
        # Search back in the data for matching sequences
        search_start = max(0, i - 4096)
        for j in range(search_start, i):
            match_length = 0
            
            # Check how many bytes match
            while (i + match_length < len(data) and 
                   j + match_length < i and 
                   data[j + match_length] == data[i + match_length] and 
                   match_length < 32):
                match_length += 1
            
            # Update best match if this is better
            if match_length > best_match_length:
                best_match_length = match_length
                best_match_offset = i - j
        
        # Decide how to encode
        if best_match_length > 2:
            # Compressed sequence: encode length and offset
            # Ensure the byte stays within 0-255 range
            first_byte = min(255, best_match_length | ((best_match_offset & 0x0F) << 5))
            second_byte = min(255, best_match_offset >> 4)
            
            compressed.append(first_byte)
            compressed.append(second_byte)
            i += best_match_length
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
        first_byte = compressed_data[i]
        
        # Check if this is a compressed sequence
        if first_byte & 0x1F != first_byte:
            # Compressed sequence
            match_length = first_byte & 0x1F
            
            # Ensure we have a second byte
            if i + 1 >= len(compressed_data):
                raise ValueError("Invalid compressed data")
            
            # Extract offset
            offset_high = compressed_data[i + 1]
            match_offset = ((first_byte & 0xE0) >> 5) | (offset_high << 4)
            
            # Sanity check for start index
            if match_offset == 0 or match_offset > len(decompressed):
                raise ValueError("Invalid match offset")
            
            # Reconstruct matching sequence
            start = len(decompressed) - match_offset
            for j in range(match_length):
                if start + j >= len(decompressed):
                    break
                decompressed.append(decompressed[start + j])
            
            # Move past the two bytes used for compressed sequence
            i += 2
        else:
            # Literal byte
            decompressed.append(first_byte)
            i += 1
    
    return bytes(decompressed)