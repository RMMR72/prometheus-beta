import pytest
from datetime import datetime, timedelta
from src.timestamp_diff import calculate_timestamp_difference

def test_timestamp_difference_datetime_objects():
    """Test difference between two datetime objects"""
    dt1 = datetime(2023, 1, 1, 10, 0, 0)
    dt2 = datetime(2023, 1, 1, 11, 30, 0)
    
    diff = calculate_timestamp_difference(dt1, dt2)
    assert diff == timedelta(hours=1, minutes=30)

def test_timestamp_difference_string_inputs():
    """Test difference with timestamp strings"""
    diff1 = calculate_timestamp_difference(
        "2023-01-01 10:00:00", 
        "2023-01-01 11:30:00"
    )
    assert diff1 == timedelta(hours=1, minutes=30)

def test_timestamp_difference_mixed_inputs():
    """Test difference with mixed input types"""
    dt = datetime(2023, 1, 1, 10, 0, 0)
    str_dt = "2023-01-01 11:30:00"
    
    diff = calculate_timestamp_difference(dt, str_dt)
    assert diff == timedelta(hours=1, minutes=30)

def test_timestamp_difference_absolute_value():
    """Test that difference is always positive"""
    dt1 = datetime(2023, 1, 1, 11, 30, 0)
    dt2 = datetime(2023, 1, 1, 10, 0, 0)
    
    diff = calculate_timestamp_difference(dt1, dt2)
    assert diff == timedelta(hours=1, minutes=30)

def test_same_timestamp():
    """Test timestamps that are exactly the same"""
    dt = datetime(2023, 1, 1, 10, 0, 0)
    
    diff = calculate_timestamp_difference(dt, dt)
    assert diff == timedelta(0)

def test_invalid_string_format():
    """Test invalid string timestamp format"""
    with pytest.raises(ValueError):
        calculate_timestamp_difference("invalid-format", "2023-01-01")

def test_invalid_input_type():
    """Test invalid input types"""
    with pytest.raises(TypeError):
        calculate_timestamp_difference(123, "2023-01-01")
    with pytest.raises(TypeError):
        calculate_timestamp_difference("2023-01-01", [1, 2, 3])