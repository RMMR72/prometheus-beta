class ListNode:
    """
    A class representing a node in a singly linked list.
    
    Attributes:
        val (Any): The value stored in the node.
        next (ListNode, optional): Reference to the next node in the list. Defaults to None.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    """
    Reverse a singly linked list in-place.
    
    This function reverses the links of a singly linked list, modifying the original list.
    
    Args:
        head (ListNode): The head of the input linked list.
    
    Returns:
        ListNode: The new head of the reversed linked list.
    
    Time Complexity: O(n), where n is the number of nodes in the list
    Space Complexity: O(1), as reversal is done in-place
    
    Examples:
        # Empty list
        >>> reverse_linked_list(None) is None
        True
        
        # Single node list
        >>> node = ListNode(1)
        >>> reversed_node = reverse_linked_list(node)
        >>> reversed_node.val
        1
        >>> reversed_node.next is None
        True
        
        # Multiple node list
        >>> head = ListNode(1, ListNode(2, ListNode(3)))
        >>> reversed = reverse_linked_list(head)
        >>> reversed.val
        3
        >>> reversed.next.val
        2
        >>> reversed.next.next.val
        1
        >>> reversed.next.next.next is None
        True
    """
    # Handle empty list case
    if not head:
        return None
    
    # Handle single node case
    if not head.next:
        return head
    
    # Multiple node reversal
    prev = None
    current = head
    
    while current:
        # Store the next node before changing links
        next_node = current.next
        
        # Reverse the link
        current.next = prev
        
        # Move pointers forward
        prev = current
        current = next_node
    
    # Return the new head (which was originally the last node)
    return prev