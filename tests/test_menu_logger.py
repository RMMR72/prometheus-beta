import os
import logging
import pytest
from src.menu_logger import MenuLogger

class TestMenuLogger:
    def setup_method(self):
        """Setup method to create a temporary log file for each test."""
        # Ensure the directory exists
        os.makedirs('logs', exist_ok=True)
        self.log_file = os.path.join('logs', 'test_menu_log.log')
        
        # Configure a test-specific logger
        self.logger = logging.getLogger('test_menu_logger')
        self.logger.setLevel(logging.INFO)
        
        # Create a FileHandler
        file_handler = logging.FileHandler(self.log_file, mode='w')
        file_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(message)s')
        file_handler.setFormatter(formatter)
        
        # Add the FileHandler to the logger
        self.logger.addHandler(file_handler)
    
    def teardown_method(self):
        """Clean up the log file and remove handlers after each test."""
        # Remove all handlers to prevent duplicate logging
        while self.logger.handlers:
            self.logger.removeHandler(self.logger.handlers[0])
        
        if os.path.exists(self.log_file):
            os.remove(self.log_file)
    
    def test_log_single_selection(self):
        """Test logging a single menu selection."""
        menu_logger = MenuLogger(self.log_file)
        menu_logger.log_selection('Main Menu', 'Option 1')
        
        # Verify log file contents
        assert os.path.exists(self.log_file), "Log file was not created"
        with open(self.log_file, 'r') as f:
            log_content = f.read()
            assert "Main Menu' - Selected: Option 1" in log_content
    
    def test_log_multiple_selections(self):
        """Test logging multiple menu selections."""
        menu_logger = MenuLogger(self.log_file)
        selections = ['Option 1', 'Option 2', 'Option 3']
        menu_logger.log_multiple_selections('Main Menu', selections)
        
        # Verify log file contents
        assert os.path.exists(self.log_file), "Log file was not created"
        with open(self.log_file, 'r') as f:
            log_content = f.read()
            for selection in selections:
                assert f"Main Menu' - Selected: {selection}" in log_content
    
    def test_empty_menu_name_raises_error(self):
        """Test that empty menu name raises a ValueError."""
        menu_logger = MenuLogger(self.log_file)
        
        with pytest.raises(ValueError, match="Menu name cannot be empty"):
            menu_logger.log_selection('', 'Option')
        
        with pytest.raises(ValueError, match="Menu name cannot be empty"):
            menu_logger.log_multiple_selections('', ['Option'])
    
    def test_invalid_selections_type(self):
        """Test that non-list selections raise a TypeError."""
        menu_logger = MenuLogger(self.log_file)
        
        with pytest.raises(TypeError, match="Selections must be a list"):
            menu_logger.log_multiple_selections('Main Menu', 'Not a list')
    
    def test_log_different_selection_types(self):
        """Test logging selections of different types."""
        menu_logger = MenuLogger(self.log_file)
        selections = [
            'String Option', 
            42, 
            3.14, 
            True, 
            ['Nested', 'List'], 
            {'key': 'value'}
        ]
        
        menu_logger.log_multiple_selections('Diverse Menu', selections)
        
        # Verify log file contents
        assert os.path.exists(self.log_file), "Log file was not created"
        with open(self.log_file, 'r') as f:
            log_content = f.read()
            for selection in selections:
                assert f"Diverse Menu' - Selected: {selection}" in log_content
    
    def test_console_logging(self):
        """Test logging to console when no log file is specified."""
        menu_logger = MenuLogger()
        # This test ensures no exception is raised when logging to console
        menu_logger.log_selection('Console Menu', 'Option 1')
        menu_logger.log_multiple_selections('Console Menu', ['Option 2', 'Option 3'])