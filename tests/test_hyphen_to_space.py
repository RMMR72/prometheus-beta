import pytest
from src.hyphen_to_space import replace_hyphens_with_spaces

def test_replace_hyphens_with_spaces_basic():
    """Test basic hyphen replacement."""
    assert replace_hyphens_with_spaces('hello-world') == 'hello world'

def test_replace_hyphens_with_spaces_multiple_hyphens():
    """Test replacement with multiple hyphens."""
    assert replace_hyphens_with_spaces('hello-beautiful-world') == 'hello beautiful world'

def test_replace_hyphens_with_spaces_no_hyphens():
    """Test string with no hyphens."""
    assert replace_hyphens_with_spaces('helloworld') == 'helloworld'

def test_replace_hyphens_with_spaces_empty_string():
    """Test empty string."""
    assert replace_hyphens_with_spaces('') == ''

def test_replace_hyphens_with_spaces_invalid_input():
    """Test invalid input type raises TypeError."""
    with pytest.raises(TypeError):
        replace_hyphens_with_spaces(123)
    with pytest.raises(TypeError):
        replace_hyphens_with_spaces(None)