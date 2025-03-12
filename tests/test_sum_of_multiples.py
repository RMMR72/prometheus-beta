import pytest
from src.sum_of_multiples import sum_of_multiples

def test_basic_multiple():
    """Test basic multiple scenario"""
    assert sum_of_multiples(10, [3, 5]) == 23  # 3 + 5 + 6 + 9 + 10

def test_single_multiple():
    """Test with a single multiple"""
    assert sum_of_multiples(10, [3]) == 18  # 3 + 6 + 9

def test_multiple_large_limit():
    """Test with a larger limit"""
    assert sum_of_multiples(1000, [3, 5]) == 233168

def test_empty_multiples():
    """Test with an empty list of multiples"""
    assert sum_of_multiples(10, []) == 0

def test_no_multiples():
    """Test when no multiples exist"""
    assert sum_of_multiples(3, [7]) == 0

def test_invalid_limit_zero():
    """Test that zero limit raises ValueError"""
    with pytest.raises(ValueError, match="Limit must be a positive integer"):
        sum_of_multiples(0, [3, 5])

def test_invalid_limit_negative():
    """Test that negative limit raises ValueError"""
    with pytest.raises(ValueError, match="Limit must be a positive integer"):
        sum_of_multiples(-10, [3, 5])

def test_invalid_multiple_zero():
    """Test that zero in multiples raises ValueError"""
    with pytest.raises(ValueError, match="All multiples must be positive integers"):
        sum_of_multiples(10, [0, 5])

def test_invalid_multiple_negative():
    """Test that negative multiple raises ValueError"""
    with pytest.raises(ValueError, match="All multiples must be positive integers"):
        sum_of_multiples(10, [-3, 5])

def test_duplicate_multiples():
    """Test handling of duplicate multiples"""
    assert sum_of_multiples(10, [3, 3, 5]) == 23  # Should be same as basic multiple test

def test_large_multiples():
    """Test with large multiples"""
    assert sum_of_multiples(20, [7, 11]) == 77  # 7 + 11 + 14 + 21