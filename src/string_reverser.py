def reverse_string_in_place(s: list) -> None:
    """
    Reverse the characters of a list-like string in-place without using extra memory.
    
    This function modifies the input string by reversing its characters directly.
    It works with mutable sequences like list of characters.
    
    Args:
        s (list): A mutable sequence of characters to be reversed in-place.
    
    Raises:
        TypeError: If the input is not a mutable sequence.
    
    Examples:
        >>> chars = list('hello')
        >>> reverse_string_in_place(chars)
        >>> chars
        ['o', 'l', 'l', 'e', 'h']
    """
    # Check if input is a mutable sequence
    if not hasattr(s, '__setitem__'):
        raise TypeError("Input must be a mutable sequence like list")
    
    # Get the length of the sequence
    length = len(s)
    
    # Use two-pointer technique to swap characters
    left, right = 0, length - 1
    while left < right:
        # Swap characters
        s[left], s[right] = s[right], s[left]
        
        # Move pointers inward
        left += 1
        right -= 1