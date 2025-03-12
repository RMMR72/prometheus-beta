"""
Test suite for LZVN compression algorithm implementation
"""

import pytest
import sys
import os

# Add project root to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.lzvn_compression import compress_lzvn, decompress_lzvn

def test_compress_decompress_simple():
    """Test basic compression and decompression"""
    original_data = b'hello world hello world'
    compressed = compress_lzvn(original_data)
    assert compressed != original_data
    decompressed = decompress_lzvn(compressed)
    assert decompressed == original_data

def test_compress_decompress_repeated_pattern():
    """Test compression and decompression with repeated patterns"""
    original_data = b'abcabcabcabcabcabc' * 10
    compressed = compress_lzvn(original_data)
    assert len(compressed) < len(original_data)
    decompressed = decompress_lzvn(compressed)
    assert decompressed == original_data

def test_compress_decompress_large_data():
    """Test with a larger dataset"""
    original_data = b'\x00\x01\x02\x03' * 1000
    compressed = compress_lzvn(original_data)
    assert len(compressed) < len(original_data)
    decompressed = decompress_lzvn(compressed)
    assert decompressed == original_data

def test_empty_input_raises_error():
    """Test that empty input raises ValueError"""
    with pytest.raises(ValueError):
        compress_lzvn(b'')
    with pytest.raises(ValueError):
        decompress_lzvn(b'')

def test_invalid_input_type():
    """Test that non-bytes input raises TypeError"""
    with pytest.raises(TypeError):
        compress_lzvn('not bytes')
    with pytest.raises(TypeError):
        decompress_lzvn('not bytes')

def test_single_byte_data():
    """Test compression and decompression of single byte"""
    original_data = b'\xFF'
    compressed = compress_lzvn(original_data)
    decompressed = decompress_lzvn(compressed)
    assert decompressed == original_data
    
def test_compression_size_decrease():
    """Verify that compression reduces data size for repetitive content"""
    original_data = b'compress me compress me' * 100
    compressed = compress_lzvn(original_data)
    assert len(compressed) < len(original_data)

def test_edge_case_no_repetition():
    """Test compression of data with no repetition"""
    original_data = bytes(range(256))
    compressed = compress_lzvn(original_data)
    decompressed = decompress_lzvn(compressed)
    assert decompressed == original_data