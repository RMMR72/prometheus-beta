import logging
import emoji

def log_with_emoji(message, level=logging.INFO, emoji_symbol=None):
    """
    Log a message with an optional emoji symbol.
    
    Args:
        message (str): The message to log
        level (int, optional): Logging level. Defaults to logging.INFO
        emoji_symbol (str, optional): Emoji to prepend to the message. Defaults to None
    
    Returns:
        None
    
    Raises:
        TypeError: If message is not a string
        ValueError: If emoji_symbol is not a valid emoji
    """
    # Validate input types
    if not isinstance(message, str):
        raise TypeError("Message must be a string")
    
    # Configure logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    
    # Create console handler if not exists
    if not logger.handlers:
        console_handler = logging.StreamHandler()
        formatter = logging.Formatter('%(message)s')
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    
    # Process emoji if provided
    if emoji_symbol:
        try:
            # Validate and convert emoji
            validated_emoji = emoji.emojize(emoji_symbol, language='alias')
            full_message = f"{validated_emoji} {message}"
        except TypeError:
            raise ValueError("Invalid emoji symbol")
    else:
        full_message = message
    
    # Log the message at the specified level
    if level == logging.DEBUG:
        logger.debug(full_message)
    elif level == logging.INFO:
        logger.info(full_message)
    elif level == logging.WARNING:
        logger.warning(full_message)
    elif level == logging.ERROR:
        logger.error(full_message)
    elif level == logging.CRITICAL:
        logger.critical(full_message)
    else:
        raise ValueError("Invalid logging level")