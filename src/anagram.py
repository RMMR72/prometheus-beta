def isAnagram(str1: str, str2: str) -> bool:
    """
    Determine if two strings are anagrams of each other.

    An anagram is a word or phrase formed by rearranging the letters of another word or phrase,
    using all the original letters exactly once. The function is case-insensitive and 
    ignores whitespace.

    Args:
        str1 (str): The first input string
        str2 (str): The second input string

    Returns:
        bool: True if the strings are anagrams, False otherwise

    Examples:
        >>> isAnagram("listen", "silent")
        True
        >>> isAnagram("hello", "world")
        False
    """
    # Remove whitespace and convert to lowercase
    cleaned_str1 = ''.join(str1.lower().split())
    cleaned_str2 = ''.join(str2.lower().split())

    # Check if lengths are different
    if len(cleaned_str1) != len(cleaned_str2):
        return False

    # Create character frequency dictionaries
    char_count1 = {}
    char_count2 = {}

    # Count character frequencies
    for char in cleaned_str1:
        char_count1[char] = char_count1.get(char, 0) + 1
    
    for char in cleaned_str2:
        char_count2[char] = char_count2.get(char, 0) + 1

    # Compare character frequency dictionaries
    return char_count1 == char_count2