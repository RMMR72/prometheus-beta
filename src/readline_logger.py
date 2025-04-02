import readline
import logging
from typing import Optional, Callable

class ReadlineLogger:
    """
    A utility class for logging interactive readline prompts.
    
    This class provides methods to log user inputs during interactive sessions,
    with support for custom logging configuration and optional input validation.
    """
    
    def __init__(self, logger: Optional[logging.Logger] = None):
        """
        Initialize the ReadlineLogger.
        
        Args:
            logger (Optional[logging.Logger]): A custom logger. 
                If not provided, a default logger will be created.
        """
        self.logger = logger or logging.getLogger(__name__)
    
    def log_prompt(self, 
                   prompt: str, 
                   validator: Optional[Callable[[str], bool]] = None,
                   log_level: int = logging.INFO) -> str:
        """
        Log an interactive prompt and capture user input.
        
        Args:
            prompt (str): The prompt text to display to the user.
            validator (Optional[Callable[[str], bool]]): Optional function to validate input.
            log_level (int): Logging level for the input (default: logging.INFO)
        
        Returns:
            str: The user's input
        
        Raises:
            ValueError: If input validation fails
        """
        while True:
            try:
                # Log the prompt explicitly
                self.logger.log(log_level, f"Prompt: {prompt}")
                
                # Use readline for interactive input
                user_input = input(prompt)
                
                # Log the input explicitly 
                self.logger.log(log_level, f"User Input: {user_input}")
                
                # Validate input if a validator is provided
                if validator:
                    if not validator(user_input):
                        self.logger.error("Input validation failed")
                        print("Invalid input. Please try again.")
                        continue
                
                return user_input
            
            except ValueError as e:
                # Log validation errors
                self.logger.error(f"Input validation error: {e}")
                print(f"Invalid input. {e}")
            except Exception as e:
                # Log unexpected errors
                self.logger.error(f"Unexpected error during input: {e}")
                raise