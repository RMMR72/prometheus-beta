import psutil
import logging
import os

def log_memory_usage(logger=None):
    """
    Log current memory usage statistics.
    
    Args:
        logger (logging.Logger, optional): Logger to use for reporting. 
                                           If None, creates a default logger.
    
    Returns:
        dict: A dictionary containing memory usage statistics
    """
    # Create a default logger if none is provided
    if logger is None:
        logger = logging.getLogger(__name__)
        # Configure basic logging if no handler exists
        if not logger.handlers:
            logging.basicConfig(level=logging.INFO, 
                                format='%(asctime)s - %(levelname)s - %(message)s')
    
    try:
        # Get memory information
        memory = psutil.virtual_memory()
        
        # Prepare memory statistics
        memory_stats = {
            'total_memory': memory.total / (1024 * 1024),  # Convert to MB
            'available_memory': memory.available / (1024 * 1024),  # Convert to MB
            'used_memory': memory.used / (1024 * 1024),  # Convert to MB
            'memory_percent': memory.percent
        }
        
        # Log the memory statistics
        logger.info(f"Memory Usage Statistics: {memory_stats}")
        
        return memory_stats
    
    except Exception as e:
        logger.error(f"Error collecting memory usage statistics: {str(e)}")
        raise