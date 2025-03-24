import pytest
import logging
import io
import sys
from src.emoji_logger import log_with_emoji

def test_log_default_message(caplog):
    """Test logging a basic message"""
    caplog.set_level(logging.INFO)
    log_with_emoji("Test message")
    assert "Test message" in caplog.text

def test_log_with_emoji(caplog):
    """Test logging a message with an emoji"""
    caplog.set_level(logging.INFO)
    log_with_emoji("Hello", emoji_symbol=":wave:")
    assert "👋 Hello" in caplog.text

def test_different_log_levels(caplog):
    """Test logging at different levels"""
    # Test each log level
    log_levels = [
        (logging.DEBUG, "Debug message"),
        (logging.INFO, "Info message"),
        (logging.WARNING, "Warning message"),
        (logging.ERROR, "Error message"),
        (logging.CRITICAL, "Critical message")
    ]
    
    for level, message in log_levels:
        caplog.clear()
        caplog.set_level(level)
        log_with_emoji(message, level=level, emoji_symbol=":star:")
        assert "⭐" in caplog.text
        assert message in caplog.text

def test_invalid_message_type():
    """Test that TypeError is raised for non-string message"""
    with pytest.raises(TypeError, match="Message must be a string"):
        log_with_emoji(123)

def test_invalid_emoji():
    """Test that ValueError is raised for invalid emoji"""
    with pytest.raises(ValueError, match="Invalid emoji symbol"):
        log_with_emoji("Test", emoji_symbol="not_an_emoji")

def test_invalid_log_level():
    """Test that ValueError is raised for invalid log level"""
    with pytest.raises(ValueError, match="Invalid logging level"):
        log_with_emoji("Test", level=999)