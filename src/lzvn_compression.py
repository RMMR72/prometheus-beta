"""
LZVN-like Compression Algorithm Implementation

This module provides a simplified compression algorithm 
inspired by dictionary and run-length techniques.
"""

def compress_lzvn(data):
    """
    Compress input data using a simplified LZVN-like algorithm.
    
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
        # Search for repeats within a limited window
        max_match_length = 0
        max_match_offset = 0
        
        # Limit search window
        search_start = max(0, i - 256)
        for j in range(search_start, i):
            match_length = 0
            
            # Check sequence match
            while (i + match_length < len(data) and 
                   j + match_length < i and 
                   data[j + match_length] == data[i + match_length] and 
                   match_length < 15):
                match_length += 1
            
            # Update best match
            if match_length > max_match_length:
                max_match_length = match_length
                max_match_offset = i - j
        
        # Encode sequence
        if max_match_length > 2:
            # Compressed encoding
            # Use 4 bits for match length, 4 bits for offset low byte
            first_byte = ((max_match_length & 0x0F) << 4) | (max_match_offset & 0x0F)
            second_byte = (max_match_offset >> 4) & 0xFF
            
            compressed.append(first_byte)
            compressed.append(second_byte)
            i += max_match_length
        else:
            # Literal byte
            compressed.append(data[i])
            i += 1
    
    # Ensure we have some compression
    if len(compressed) >= len(data):
        # If no compression achieved, signal this by setting first bit
        compressed = bytearray([0x80]) + data
    
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
    
    # Check for uncompressed signal
    if compressed_data[0] == 0x80:
        return compressed_data[1:]
    
    decompressed = bytearray()
    i = 0
    
    while i < len(compressed_data):
        first_byte = compressed_data[i]
        
        # Check for compressed sequence
        if first_byte & 0xF0 != first_byte:
            # Sequence information in first byte
            match_length = (first_byte & 0xF0) >> 4
            
            # Ensure second byte exists
            if i + 1 >= len(compressed_data):
                decompressed.append(first_byte)
                break
            
            # Extract offset
            offset_low = first_byte & 0x0F
            offset_high = compressed_data[i + 1]
            match_offset = (offset_high << 4) | offset_low
            
            # Validate offset
            if match_offset == 0 or match_offset > len(decompressed):
                decompressed.append(first_byte)
                i += 1
                continue
            
            # Reproduce matching sequence
            start = len(decompressed) - match_offset
            for _ in range(match_length):
                if start < len(decompressed):
                    decompressed.append(decompressed[start])
                    start += 1
            
            i += 2
        else:
            # Literal byte
            decompressed.append(first_byte)
            i += 1
    
    return bytes(decompressed)