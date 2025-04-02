import pytest
from src.dot_case_converter import to_dot_case

def test_to_dot_case_basic_conversions():
    """Test basic string conversions to dot case."""
    assert to_dot_case("HelloWorld") == "hello.world"
    assert to_dot_case("hello_world") == "hello.world"
    assert to_dot_case("Hello World") == "hello.world"
    assert to_dot_case("hello-world") == "hello.world"

def test_to_dot_case_edge_cases():
    """Test edge cases for dot case conversion."""
    assert to_dot_case("") == ""
    assert to_dot_case("   ") == ""
    assert to_dot_case("a") == "a"
    assert to_dot_case("A") == "a"

def test_to_dot_case_multiple_words():
    """Test conversion with multiple words and different separators."""
    assert to_dot_case("Hello_World_Test") == "hello.world.test"
    assert to_dot_case("hello-world-test") == "hello.world.test"
    assert to_dot_case("Hello World Test") == "hello.world.test"

def test_to_dot_case_mixed_separators():
    """Test conversion with mixed separators."""
    assert to_dot_case("hello_World-Test foo") == "hello.world.test.foo"

def test_to_dot_case_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        to_dot_case(None)
    with pytest.raises(TypeError):
        to_dot_case(123)
    with pytest.raises(TypeError):
        to_dot_case(["hello", "world"])