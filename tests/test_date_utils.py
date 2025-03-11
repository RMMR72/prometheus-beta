import pytest
from datetime import date
from src.date_utils import get_day_name

def test_get_day_name_with_date_object():
    """Test getting day name with a date object."""
    assert get_day_name(date(2023, 6, 21)) == 'Wednesday'

def test_get_day_name_with_valid_string():
    """Test getting day name with a valid date string."""
    assert get_day_name('2023-06-21') == 'Wednesday'

def test_get_day_name_different_dates():
    """Test multiple different dates."""
    test_cases = [
        (date(2023, 1, 1), 'Sunday'),     # New Year's Day
        (date(2023, 12, 25), 'Monday'),   # Christmas Day
        (date(2024, 2, 29), 'Thursday')   # Leap day
    ]
    
    for test_date, expected_day in test_cases:
        assert get_day_name(test_date) == expected_day

def test_invalid_date_string():
    """Test that invalid date string raises ValueError."""
    with pytest.raises(ValueError, match="Invalid date string"):
        get_day_name('invalid-date')

def test_invalid_date_format():
    """Test that incorrectly formatted date string raises ValueError."""
    with pytest.raises(ValueError, match="Invalid date string"):
        get_day_name('21-06-2023')  # wrong format

def test_invalid_input_type():
    """Test that invalid input type raises TypeError."""
    with pytest.raises(TypeError, match="Input must be a date object"):
        get_day_name(12345)
    
    with pytest.raises(TypeError, match="Input must be a date object"):
        get_day_name(None)

def test_edge_cases():
    """Test various edge cases."""
    # Test earliest possible date
    assert get_day_name(date(1, 1, 1)) == 'Monday'
    
    # Test far future date
    assert get_day_name(date(2050, 12, 31)) == 'Sunday'