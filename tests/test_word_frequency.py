import os
import pytest
from src.word_frequency import analyze_word_frequency

@pytest.fixture
def sample_word_file(tmp_path):
    """Create a temporary file with sample words for testing."""
    file_path = tmp_path / "sample_words.txt"
    file_path.write_text("apple, banana, apple, cherry, banana, date")
    return str(file_path)

def test_word_frequency_basic(sample_word_file):
    """Test basic word frequency counting."""
    result = analyze_word_frequency(sample_word_file)
    expected = {'apple': 2, 'banana': 2, 'cherry': 1, 'date': 1}
    assert result == expected

def test_word_frequency_empty_file(tmp_path):
    """Test handling of an empty file."""
    empty_file = tmp_path / "empty.txt"
    empty_file.write_text("")
    
    with pytest.raises(ValueError, match="File is empty"):
        analyze_word_frequency(str(empty_file))

def test_word_frequency_nonexistent_file():
    """Test handling of a nonexistent file."""
    with pytest.raises(FileNotFoundError):
        analyze_word_frequency("nonexistent_file.txt")

def test_word_frequency_case_insensitive(tmp_path):
    """Test that word counting is case-insensitive."""
    file_path = tmp_path / "case_test.txt"
    file_path.write_text("Apple, apple, APPLE, banana")
    
    result = analyze_word_frequency(str(file_path))
    expected = {'apple': 3, 'banana': 1}
    assert result == expected

def test_word_frequency_extra_spaces(tmp_path):
    """Test handling of extra spaces and commas."""
    file_path = tmp_path / "spaces_test.txt"
    file_path.write_text("  apple ,  banana,  apple  , cherry ")
    
    result = analyze_word_frequency(str(file_path))
    expected = {'apple': 2, 'banana': 1, 'cherry': 1}
    assert result == expected

def test_word_frequency_empty_input():
    """Test handling of empty file path."""
    with pytest.raises(ValueError, match="File path cannot be empty"):
        analyze_word_frequency("")