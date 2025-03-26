def find_local_max(arr):
    """
    Find local maximum values in an input array.
    
    A local maximum is an element that is greater than its immediate neighbors.
    
    Args:
        arr (list): Input list of numbers
    
    Returns:
        list: Indices of local maximum values
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input list is empty
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if len(arr) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Handle single element case
    if len(arr) == 1:
        return [0]
    
    local_max_indices = []
    
    # Check first element
    if arr[0] > arr[1]:
        local_max_indices.append(0)
    
    # Check middle elements
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            local_max_indices.append(i)
    
    # Check last element
    if arr[-1] > arr[-2]:
        local_max_indices.append(len(arr) - 1)
    
    return local_max_indices