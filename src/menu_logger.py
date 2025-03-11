import logging
import os
from typing import List, Any, Optional

class MenuLogger:
    """
    A class to log user selections from a menu with various logging options.
    
    Attributes:
        log_file (Optional[str]): Path to the log file. If None, logs to console.
    """
    
    def __init__(self, log_file: Optional[str] = None):
        """
        Initialize the MenuLogger.
        
        Args:
            log_file (Optional[str], optional): Path to the log file. Defaults to None.
        """
        # Ensure directory exists for log file
        if log_file:
            os.makedirs(os.path.dirname(log_file) or '.', exist_ok=True)
        
        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            filename=log_file if log_file else None,
            filemode='a'  # Append mode to prevent overwriting
        )
        self.logger = logging.getLogger(__name__)
    
    def log_selection(self, menu_name: str, selection: Any) -> None:
        """
        Log a user's menu selection.
        
        Args:
            menu_name (str): Name or identifier of the menu.
            selection (Any): The selected item from the menu.
        
        Raises:
            ValueError: If menu_name is empty or None.
        """
        # Validate input
        if not menu_name:
            raise ValueError("Menu name cannot be empty")
        
        # Log the selection
        log_message = f"Menu '{menu_name}' - Selected: {selection}"
        self.logger.info(log_message)
    
    def log_multiple_selections(self, menu_name: str, selections: List[Any]) -> None:
        """
        Log multiple selections from a menu.
        
        Args:
            menu_name (str): Name or identifier of the menu.
            selections (List[Any]): List of selected items from the menu.
        
        Raises:
            ValueError: If menu_name is empty or None.
            TypeError: If selections is not a list.
        """
        # Validate input
        if not menu_name:
            raise ValueError("Menu name cannot be empty")
        
        if not isinstance(selections, list):
            raise TypeError("Selections must be a list")
        
        # Log multiple selections
        for selection in selections:
            self.log_selection(menu_name, selection)