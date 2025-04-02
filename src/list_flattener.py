def flatten_nested_list(nested_list):
    """
    Flatten a nested list into a single-level list.
    
    This function recursively flattens a nested list of arbitrary depth.
    
    Args:
        nested_list (list): A potentially nested list to be flattened.
    
    Returns:
        list: A flattened version of the input list.
    
    Raises:
        TypeError: If the input is not a list.
    
    Examples:
        >>> flatten_nested_list([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
        >>> flatten_nested_list([])
        []
    """
    # Check if input is a list
    if not isinstance(nested_list, list):
        raise TypeError("Input must be a list")
    
    # Result list to store flattened elements
    flattened = []
    
    # Iterate through each element in the nested list
    for item in nested_list:
        # If the item is a list, recursively flatten it
        if isinstance(item, list):
            flattened.extend(flatten_nested_list(item))
        else:
            # If not a list, append the item directly
            flattened.append(item)
    
    return flattened