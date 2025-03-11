import os
import pytest
import logging
from src.menu_logger import MenuLogger

class TestMenuLogger:
    def setup_method(self):
        """Setup method to create a temporary log file for each test."""
        self.log_file = 'test_menu_log.log'
    
    def teardown_method(self):
        """Clean up the log file after each test."""
        if os.path.exists(self.log_file):
            os.remove(self.log_file)
    
    def test_log_single_selection(self):
        """Test logging a single menu selection."""
        logger = MenuLogger(self.log_file)
        logger.log_selection('Main Menu', 'Option 1')
        
        # Verify log file contents
        with open(self.log_file, 'r') as f:
            log_content = f.read()
            assert "Menu 'Main Menu' - Selected: Option 1" in log_content
    
    def test_log_multiple_selections(self):
        """Test logging multiple menu selections."""
        logger = MenuLogger(self.log_file)
        selections = ['Option 1', 'Option 2', 'Option 3']
        logger.log_multiple_selections('Main Menu', selections)
        
        # Verify log file contents
        with open(self.log_file, 'r') as f:
            log_content = f.read()
            for selection in selections:
                assert f"Menu 'Main Menu' - Selected: {selection}" in log_content
    
    def test_empty_menu_name_raises_error(self):
        """Test that empty menu name raises a ValueError."""
        logger = MenuLogger(self.log_file)
        
        with pytest.raises(ValueError, match="Menu name cannot be empty"):
            logger.log_selection('', 'Option')
        
        with pytest.raises(ValueError, match="Menu name cannot be empty"):
            logger.log_multiple_selections('', ['Option'])
    
    def test_invalid_selections_type(self):
        """Test that non-list selections raise a TypeError."""
        logger = MenuLogger(self.log_file)
        
        with pytest.raises(TypeError, match="Selections must be a list"):
            logger.log_multiple_selections('Main Menu', 'Not a list')
    
    def test_log_different_selection_types(self):
        """Test logging selections of different types."""
        logger = MenuLogger(self.log_file)
        selections = [
            'String Option', 
            42, 
            3.14, 
            True, 
            ['Nested', 'List'], 
            {'key': 'value'}
        ]
        
        logger.log_multiple_selections('Diverse Menu', selections)
        
        # Verify log file contents
        with open(self.log_file, 'r') as f:
            log_content = f.read()
            for selection in selections:
                assert f"Menu 'Diverse Menu' - Selected: {selection}" in log_content
    
    def test_console_logging(self):
        """Test logging to console when no log file is specified."""
        logger = MenuLogger()
        # This test ensures no exception is raised when logging to console
        logger.log_selection('Console Menu', 'Option 1')
        logger.log_multiple_selections('Console Menu', ['Option 2', 'Option 3'])