def count_anagrams(s):
    """
    Count the number of distinct anagrams in a given string.
    
    An anagram is a substring that contains the same characters in a different order.
    
    Args:
        s (str): Input string containing only lowercase English letters.
    
    Returns:
        int: Number of distinct anagrams in the string.
    
    Raises:
        ValueError: If the input string contains characters other than lowercase letters.
    """
    # Validate input
    if not s or not s.islower() or not s.isalpha():
        raise ValueError("Input must be a non-empty string with lowercase English letters only")
    
    # Set to store unique sorted anagram signatures
    distinct_anagrams = set()
    
    # Generate all possible substrings and their sorted signatures
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            # Get substring and create sorted signature
            substring = s[i:j]
            sorted_signature = ''.join(sorted(substring))
            distinct_anagrams.add(sorted_signature)
    
    return len(distinct_anagrams)