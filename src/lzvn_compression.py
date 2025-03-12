"""
LZVN-like Compression Algorithm Implementation

This module provides a simplified compression algorithm 
inspired by dictionary and sequence matching techniques.
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
    window_start = 0
    
    while window_start < len(data):
        # Search for best match in the previous window
        best_length = 0
        best_offset = 0
        
        # Search within a limited window
        window_end = min(window_start + 32, len(data))
        search_start = max(0, window_start - 256)
        
        for search_pos in range(search_start, window_start):
            # Attempt to match sequence
            match_length = 0
            while (window_start + match_length < window_end and 
                   search_pos + match_length < window_start and 
                   data[search_pos + match_length] == data[window_start + match_length] and 
                   match_length < 15):
                match_length += 1
            
            # Update best match
            if match_length > best_length:
                best_length = match_length
                best_offset = window_start - search_pos
        
        # Encoding strategy
        if best_length > 2:
            # Encode matched sequence
            # First byte: 4 bits length, 4 bits low offset
            first_byte = ((best_length & 0x0F) << 4) | (best_offset & 0x0F)
            # Second byte: high offset bits
            second_byte = (best_offset >> 4) & 0xFF
            
            compressed.append(first_byte)
            compressed.append(second_byte)
            window_start += best_length
        else:
            # Literal byte
            compressed.append(data[window_start])
            window_start += 1
    
    # If no compression achieved, return original with flag
    if len(compressed) >= len(data):
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
    
    # Uncompressed flag check
    if compressed_data[0] == 0x80:
        return compressed_data[1:]
    
    decompressed = bytearray()
    i = 0
    
    while i < len(compressed_data):
        first_byte = compressed_data[i]
        
        # Check for compressed sequence
        if first_byte & 0xF0 != first_byte:
            # Extract match info
            match_length = (first_byte & 0xF0) >> 4
            
            # Ensure second byte exists
            if i + 1 >= len(compressed_data):
                decompressed.append(first_byte)
                break
            
            # Reconstruct full offset
            offset_low = first_byte & 0x0F
            offset_high = compressed_data[i + 1]
            match_offset = (offset_high << 4) | offset_low
            
            # Validate and reproduce matching sequence
            if match_offset > 0 and match_offset <= len(decompressed):
                start = len(decompressed) - match_offset
                for _ in range(match_length):
                    if start < len(decompressed):
                        decompressed.append(decompressed[start])
                        start += 1
            else:
                # Invalid match, treat as literal
                decompressed.append(first_byte)
            
            i += 2
        else:
            # Literal byte
            decompressed.append(first_byte)
            i += 1
    
    return bytes(decompressed)