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
    
    # Thread-safe result list
    result = []
    result_lock = threading.Lock()
    
    # Create threads for each number
    threads = []
    for num in arr:
        def sorter(n):
            # Sleep proportional to the number's value
            time.sleep(n * 0.001)  # Scale sleep time to make sorting feasible
            with result_lock:
                result.append(n)
        
        thread = threading.Thread(target=sorter, args=(num,))
        thread.start()
        threads.append(thread)
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    return result