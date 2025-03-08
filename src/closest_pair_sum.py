def find_closest_pair_sum(arr, target):
    """
    Find the pair of elements in an array whose sum is closest to the target value.
    
    Args:
        arr (list): Input list of numbers
        target (int/float): Target sum to find closest pair to
    
    Returns:
        tuple: A tuple containing the two elements that form the closest sum to the target,
               or None if the array has fewer than 2 elements
    
    Raises:
        TypeError: If input is not a list or target is not a number
        ValueError: If the list contains non-numeric elements
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(target, (int, float)):
        raise TypeError("Target must be a number")
    
    # Check if array has at least two elements
    if len(arr) < 2:
        return None
    
    # Validate list contains only numeric elements
    if not all(isinstance(x, (int, float)) for x in arr):
        raise ValueError("All list elements must be numeric")
    
    # Initialize variables to track closest pair
    closest_sum = float('inf')
    closest_pair = None
    
    # Check all possible pairs
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            current_sum = arr[i] + arr[j]
            current_diff = abs(current_sum - target)
            
            # Update if this pair is closer to target
            if current_diff < abs(closest_sum - target):
                closest_sum = current_sum
                closest_pair = (arr[i], arr[j])
    
    return closest_pair