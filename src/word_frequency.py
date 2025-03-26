from collections import Counter
from typing import Dict, List

def analyze_word_frequency(file_path: str) -> Dict[str, int]:
    """
    Analyze the frequency of words in a text file.

    Args:
        file_path (str): Path to the text file containing words.

    Returns:
        Dict[str, int]: A dictionary of words and their frequencies, 
        sorted in descending order of frequency.

    Raises:
        FileNotFoundError: If the specified file cannot be found.
        ValueError: If the file is empty or contains invalid content.
    """
    # Validate input
    if not file_path:
        raise ValueError("File path cannot be empty")

    try:
        # Read the file content
        with open(file_path, 'r') as file:
            content = file.read().strip()

        # Check if file is empty
        if not content:
            raise ValueError("File is empty")

        # Split words, handling potential extra spaces and commas
        words = [word.strip().lower() for word in content.replace(',', ' ').split()]

        # Count word frequencies
        word_counts = Counter(words)

        # Sort by frequency in descending order
        sorted_word_counts = dict(sorted(word_counts.items(), key=lambda x: x[1], reverse=True))

        return sorted_word_counts

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        raise ValueError(f"Error processing file: {str(e)}")