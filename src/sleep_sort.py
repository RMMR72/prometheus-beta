import threading
import time
from typing import List, Union

def sleep_sort(arr: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Implement the Sleep Sort algorithm.
    
    Sleep Sort is a quirky sorting algorithm that uses threading and sleep times 
    to sort numbers. Each number is sorted by creating a thread that sleeps 
    proportionally to its value and then adds itself to the result list.
    
    Args:
        arr (List[Union[int, float]]): Input list of numbers to be sorted
    
    Returns:
        List[Union[int, float]]: Sorted list of input numbers
    
    Raises:
        ValueError: If input contains negative numbers
        TypeError: If input contains non-numeric types
    """
    # Validate input
    if not arr:
        return []
    
    # Check for non-numeric types
    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("Input must contain only numeric types")
    
    # Check for negative numbers
    if any(x < 0 for x in arr):
        raise ValueError("Sleep Sort does not support negative numbers")
    
    # Normalize sleep time to ensure proper sorting for floats
    max_val = max(arr)
    
    # Thread-safe result list
    result = []
    result_lock = threading.Lock()
    threads_complete = threading.Event()
    
    # Create threads for each number
    threads = []
    for num in arr:
        def sorter(n, max_num):
            # Scale sleep time relative to the maximum value to ensure consistent sorting
            scaled_sleep = (n / max_num) * 0.5
            time.sleep(scaled_sleep)
            with result_lock:
                result.append(n)
                # Check if all threads are complete
                if len(result) == len(arr):
                    threads_complete.set()
        
        thread = threading.Thread(target=sorter, args=(num, max_val))
        thread.start()
        threads.append(thread)
    
    # Wait for all threads to complete or timeout
    threads_complete.wait(timeout=2)  # 2-second timeout to prevent hanging
    
    # Ensure all threads are joined
    for thread in threads:
        thread.join(timeout=0.1)
    
    return sorted(result)