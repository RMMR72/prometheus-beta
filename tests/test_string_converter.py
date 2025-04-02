import pytest
from src.string_converter import to_kebab_case

def test_basic_string_conversion():
    """Test basic string to kebab case conversion."""
    assert to_kebab_case("Hello World") == "hello-world"
    assert to_kebab_case("HelloWorld") == "hello-world"

def test_different_input_formats():
    """Test conversion of different input string formats."""
    assert to_kebab_case("snake_case_string") == "snake-case-string"
    assert to_kebab_case("camelCaseString") == "camel-case-string"
    assert to_kebab_case("PascalCaseString") == "pascal-case-string"

def test_whitespace_handling():
    """Test handling of whitespace and extra spaces."""
    assert to_kebab_case("   Spaced  String   ") == "spaced-string"
    assert to_kebab_case("  ") == ""

def test_special_characters():
    """Test handling of special characters and edge cases."""
    assert to_kebab_case("Hello, World!") == "hello-world"
    assert to_kebab_case("multiple---hyphens") == "multiple-hyphens"
    assert to_kebab_case("@#$%Special Characters") == "special-characters"

def test_mixed_case_and_special_chars():
    """Test mixed case with special characters."""
    assert to_kebab_case("Mix3d_CamelCase String!") == "mix3d-camel-case-string"

def test_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        to_kebab_case(123)
    with pytest.raises(TypeError):
        to_kebab_case(None)

def test_empty_input():
    """Test empty input handling."""
    assert to_kebab_case("") == ""
    assert to_kebab_case(" ") == ""