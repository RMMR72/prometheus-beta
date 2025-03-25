import pytest
from src.ip_validator import is_valid_ip_address

def test_valid_ip_addresses():
    """Test various valid IP addresses."""
    valid_ips = [
        '0.0.0.0',
        '255.255.255.255',
        '192.168.0.1',
        '10.0.0.1',
        '172.16.0.1'
    ]
    for ip in valid_ips:
        assert is_valid_ip_address(ip) is True, f"{ip} should be valid"

def test_invalid_ip_addresses():
    """Test various invalid IP addresses."""
    invalid_ips = [
        # Out of range
        '256.0.0.1',
        '0.0.0.256',
        '-1.0.0.0',
        
        # Invalid formats
        '192.168.0',  # Too few octets
        '192.168.0.1.2',  # Too many octets
        '192.168.0.a',  # Non-numeric 
        '192.168 .0.1',  # Spaces
        
        # Leading zeros
        '01.02.03.04',
        
        # Empty strings and misc
        '',
        '   ',
        None
    ]
    for ip in invalid_ips:
        assert is_valid_ip_address(ip) is False, f"{ip} should be invalid"

def test_edge_cases():
    """Test edge case IP addresses."""
    edge_cases = [
        '0.0.0.0',  # Lowest possible
        '255.255.255.255'  # Highest possible
    ]
    for ip in edge_cases:
        assert is_valid_ip_address(ip) is True, f"{ip} should be valid"

def test_input_types():
    """Ensure the function handles different input types gracefully."""
    with pytest.raises(TypeError):
        is_valid_ip_address(None)
    
    with pytest.raises(TypeError):
        is_valid_ip_address(123)  # Non-string input