import pytest
from src.alternating_pascal_case import convert_to_alternating_pascal_case

def test_basic_conversion():
    """Test basic string conversion"""
    assert convert_to_alternating_pascal_case("hello world") == 'HelloWorld'
    assert convert_to_alternating_pascal_case("python is awesome") == 'PythonIsAwesome'

def test_mixed_case_input():
    """Test input with mixed case"""
    assert convert_to_alternating_pascal_case("PYTHON is AWESOME") == 'PythonIsAwesome'

def test_special_characters():
    """Test string with special characters"""
    assert convert_to_alternating_pascal_case("123 test case!") == 'TestCase'

def test_single_word():
    """Test single word input"""
    assert convert_to_alternating_pascal_case("hello") == 'Hello'

def test_empty_string():
    """Test empty string input"""
    assert convert_to_alternating_pascal_case("") == ''

def test_multiple_spaces():
    """Test string with multiple spaces"""
    assert convert_to_alternating_pascal_case("  python   is  great  ") == 'PythonIsGreat'

def test_error_handling():
    """Test error handling for non-string input"""
    with pytest.raises(TypeError):
        convert_to_alternating_pascal_case(123)
    with pytest.raises(TypeError):
        convert_to_alternating_pascal_case(None)

def test_symbols_and_numbers():
    """Test string with symbols and numbers"""
    assert convert_to_alternating_pascal_case("hello-world 123") == 'HelloWorld'