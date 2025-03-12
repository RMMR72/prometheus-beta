import pytest
import zlib
from src.zlib_compression import compress_data, decompress_data

def test_compress_string():
    """Test compressing a string"""
    original = "Hello, world! This is a test of Zlib compression."
    compressed = compress_data(original)
    assert isinstance(compressed, bytes)
    assert len(compressed) < len(original.encode('utf-8'))

def test_compress_bytes():
    """Test compressing bytes"""
    original = b"Binary data compression test"
    compressed = compress_data(original)
    assert isinstance(compressed, bytes)
    assert len(compressed) < len(original)

def test_decompress_string():
    """Test decompressing a compressed string"""
    original = "Hello, world! This is a test of Zlib compression."
    compressed = compress_data(original)
    decompressed = decompress_data(compressed)
    assert decompressed == original

def test_decompress_bytes():
    """Test decompressing compressed bytes"""
    original = b"Binary data compression test"
    compressed = compress_data(original)
    decompressed = decompress_data(compressed, encoding=None)
    assert decompressed == original

def test_compression_levels():
    """Test different compression levels"""
    original = "Test compression levels"
    # Test each compression level
    results = [len(compress_data(original, level)) for level in range(10)]
    # Verify that higher compression levels generally result in smaller compressed data
    assert results[0] >= results[6]  # No compression vs default
    assert results[6] >= results[9]  # Default vs max compression

def test_invalid_compression_level():
    """Test invalid compression level raises ValueError"""
    with pytest.raises(ValueError):
        compress_data("Test", compression_level=10)
    with pytest.raises(ValueError):
        compress_data("Test", compression_level=-1)

def test_invalid_input_type():
    """Test invalid input types raise TypeError"""
    with pytest.raises(TypeError):
        compress_data(123)
    with pytest.raises(TypeError):
        decompress_data("Not bytes")

def test_empty_input():
    """Test compression and decompression of empty input"""
    empty_string = ""
    empty_bytes = b""
    
    # String compression
    compressed_str = compress_data(empty_string)
    assert decompress_data(compressed_str) == empty_string
    
    # Bytes compression
    compressed_bytes = compress_data(empty_bytes)
    assert decompress_data(compressed_bytes, encoding=None) == empty_bytes

def test_large_input():
    """Test compression of large input"""
    large_input = "A" * 100000
    compressed = compress_data(large_input)
    decompressed = decompress_data(compressed)
    assert decompressed == large_input

def test_error_handling():
    """Test error handling for invalid compressed data"""
    with pytest.raises(zlib.error):
        # Try to decompress invalid data
        decompress_data(b"Invalid compressed data")