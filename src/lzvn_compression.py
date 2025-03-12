"""
LZVN-like Compression Algorithm Implementation

This module provides a simplified compression and decompression 
implementation inspired by LZVN compression principles.
"""

def compress_lzvn(data):
    """
    Compress input data using a simplified LZVN-like compression algorithm.
    
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
        # Very conservative matching to prevent data loss
        best_match_length = 0
        best_match_offset = 0
        
        # Search only within a limited window
        search_start = max(0, i - 256)  # Smaller search window
        for j in range(search_start, i):
            # Check sequence match with strict constraints
            current_match_length = 0
            while (i + current_match_length < len(data) and 
                   j + current_match_length < i and 
                   data[j + current_match_length] == data[i + current_match_length] and 
                   current_match_length < 15):  # Very limited match length
                current_match_length += 1
            
            # Update best match with preference for longer matches
            if current_match_length > best_match_length:
                best_match_length = current_match_length
                best_match_offset = i - j
        
        # More conservative matching criteria
        if best_match_length > 2:
            # Encode compressed sequence
            # Use 4 bits for length and 4 bits for offset to maintain byte range
            first_byte = ((best_match_length & 0x0F) << 4) | (best_match_offset & 0x0F)
            compressed.append(first_byte)
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
        
        # Check for compressed sequence
        if first_byte & 0xF0 != first_byte:
            # Compressed sequence
            # Extract match length (upper 4 bits)
            match_length = (first_byte & 0xF0) >> 4
            
            # Extract offset (lower 4 bits)
            match_offset = first_byte & 0x0F
            
            # Validate match offset
            if match_offset == 0 or match_offset > len(decompressed):
                # If invalid, treat as literal
                decompressed.append(first_byte)
                i += 1
                continue
            
            # Safely copy matching sequence
            start = len(decompressed) - match_offset
            
            # Limit match length to available data
            match_length = min(match_length, len(decompressed) - start)
            
            for j in range(match_length):
                decompressed.append(decompressed[start + j])
            
            i += 1
        else:
            # Literal byte
            decompressed.append(first_byte)
            i += 1
    
    return bytes(decompressed)