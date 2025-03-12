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
        # Search back for repeated sequences
        best_match_length = 0
        best_match_offset = 0
        
        # Search window limited to last 4096 bytes
        search_start = max(0, i - 4096)
        for j in range(search_start, i):
            current_match_length = 0
            
            # Check sequence match
            while (i + current_match_length < len(data) and 
                   j + current_match_length < i and 
                   data[j + current_match_length] == data[i + current_match_length] and 
                   current_match_length < 32):
                current_match_length += 1
            
            # Update best match
            if current_match_length > best_match_length:
                best_match_length = current_match_length
                best_match_offset = i - j
        
        # Decide encoding strategy
        if best_match_length > 2:
            # Encode compressed sequence
            # Lower 5 bits for length
            length_bits = best_match_length & 0x1F
            
            # Upper 3 bits of first byte for lower offset bits
            offset_low_bits = (best_match_offset & 0x7) << 5
            first_byte = length_bits | offset_low_bits
            
            # Second byte for remaining offset bits
            second_byte = best_match_offset >> 3
            
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
        
        # Check for compressed sequence
        if first_byte & 0x1F != first_byte:
            # Compressed sequence
            # Extract match length (lower 5 bits)
            match_length = first_byte & 0x1F
            
            # Ensure second byte exists
            if i + 1 >= len(compressed_data):
                break
            
            # Extract offset
            offset_low_bits = (first_byte & 0xE0) >> 5
            offset_high_bits = compressed_data[i + 1]
            match_offset = (offset_high_bits << 3) | offset_low_bits
            
            # Prevent potential out-of-bounds access
            if match_offset > len(decompressed):
                # Handle impossible matches by treating as literal
                decompressed.append(first_byte)
                i += 1
                continue
            
            # Reconstruct matching sequence
            try:
                start = len(decompressed) - match_offset
                for j in range(match_length):
                    decompressed.append(decompressed[start + j])
            except IndexError:
                # Fallback if match reconstruction fails
                decompressed.append(first_byte)
                i += 1
                continue
            
            # Move past two bytes used for compressed sequence
            i += 2
        else:
            # Literal byte
            decompressed.append(first_byte)
            i += 1
    
    return bytes(decompressed)