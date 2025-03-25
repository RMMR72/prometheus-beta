def is_valid_ip_address(ip_string: str) -> bool:
    """
    Check if a given string is a valid IPv4 address.

    Args:
        ip_string (str): The string to validate as an IP address.

    Returns:
        bool: True if the string is a valid IPv4 address, False otherwise.

    Raises:
        TypeError: If input is not a string.

    Examples:
        >>> is_valid_ip_address('192.168.0.1')
        True
        >>> is_valid_ip_address('256.0.0.1')
        False
        >>> is_valid_ip_address('192.168.0')
        False
    """
    # Type checking
    if not isinstance(ip_string, str):
        raise TypeError("Input must be a string")
    
    # Remove any whitespace
    ip_string = ip_string.strip()
    
    # Check if the IP string contains exactly 4 octets
    octets = ip_string.split('.')
    
    # Validate number of octets
    if len(octets) != 4:
        return False
    
    # Validate each octet
    for octet in octets:
        # Check for whitespace within the octet
        if ' ' in octet:
            return False
        
        # Check if octet is a valid integer
        try:
            # Convert to integer and check range
            num = int(octet)
            if num < 0 or num > 255:
                return False
            
            # Ensure no leading zeros (except for 0 itself)
            if len(octet) > 1 and octet[0] == '0':
                return False
        
        except ValueError:
            # Not a valid integer
            return False
    
    return True