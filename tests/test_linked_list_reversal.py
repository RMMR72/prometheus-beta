import pytest
from src.linked_list_reversal import ListNode, reverse_linked_list

def list_to_array(head):
    """Helper function to convert linked list to array for easy comparison."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def test_empty_list_reversal():
    """Test reversing an empty list."""
    assert reverse_linked_list(None) is None

def test_single_node_list_reversal():
    """Test reversing a list with a single node."""
    node = ListNode(1)
    reversed_list = reverse_linked_list(node)
    assert reversed_list.val == 1
    assert reversed_list.next is None

def test_multiple_node_list_reversal():
    """Test reversing a list with multiple nodes."""
    # Create a list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1, 
              ListNode(2, 
                ListNode(3, 
                  ListNode(4, 
                    ListNode(5)))))
    
    # Reverse the list
    reversed_list = reverse_linked_list(head)
    
    # Check the values are in the correct order
    assert list_to_array(reversed_list) == [5, 4, 3, 2, 1]

def test_two_node_list_reversal():
    """Test reversing a list with two nodes."""
    head = ListNode(1, ListNode(2))
    reversed_list = reverse_linked_list(head)
    assert list_to_array(reversed_list) == [2, 1]

def test_reversal_preserves_structure():
    """Ensure that the reversal correctly breaks and relinks nodes."""
    # Create a list: 1 -> 2 -> 3
    head = ListNode(1, 
              ListNode(2, 
                ListNode(3)))
    
    # Reverse the list
    reversed_list = reverse_linked_list(head)
    
    # Verify the new list structure
    assert reversed_list.val == 3
    assert reversed_list.next.val == 2
    assert reversed_list.next.next.val == 1
    assert reversed_list.next.next.next is None