import pytest
from src.lcm_recursive import lcm_recursive, gcd_recursive

def test_gcd_recursive_basic():
    """Test basic GCD calculations"""
    assert gcd_recursive(48, 18) == 6
    assert gcd_recursive(54, 24) == 6
    assert gcd_recursive(17, 5) == 1

def test_gcd_recursive_zero():
    """Test GCD with zero"""
    assert gcd_recursive(0, 5) == 5
    assert gcd_recursive(5, 0) == 5
    assert gcd_recursive(0, 0) == 0

def test_gcd_recursive_negative():
    """Test GCD with negative numbers"""
    assert gcd_recursive(-48, 18) == 6
    assert gcd_recursive(48, -18) == 6
    assert gcd_recursive(-48, -18) == 6

def test_lcm_recursive_basic():
    """Test basic LCM calculations"""
    assert lcm_recursive(4, 6) == 12
    assert lcm_recursive(21, 6) == 42
    assert lcm_recursive(17, 5) == 85

def test_lcm_recursive_zero():
    """Test LCM with zero"""
    assert lcm_recursive(0, 5) == 0
    assert lcm_recursive(5, 0) == 0
    assert lcm_recursive(0, 0) == 0

def test_lcm_recursive_negative():
    """Test LCM with negative numbers"""
    assert lcm_recursive(-4, 6) == 12
    assert lcm_recursive(4, -6) == 12
    assert lcm_recursive(-4, -6) == 12

def test_lcm_recursive_large_numbers():
    """Test LCM with larger numbers"""
    assert lcm_recursive(123, 456) == 18696

def test_lcm_recursive_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError):
        lcm_recursive(3.14, 5)
    with pytest.raises(ValueError):
        lcm_recursive(5, "not a number")