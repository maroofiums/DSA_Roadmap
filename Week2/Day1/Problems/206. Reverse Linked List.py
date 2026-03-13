class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        while current:
            next_node = current.next  # Store the next node
            current.next = prev       # Reverse the link
            prev = current            # Move prev to current
            current = next_node       # Move to the next node
        return prev  # At the end, prev will be the new head of the reversed list

# Test cases
if __name__ == "__main__":
    # Test case 1: Reversing a list of multiple nodes
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(3)
    head1.next.next.next = ListNode(4)
    head1.next.next.next.next = ListNode(5)
    
    reversed_head1 = Solution().reverseList(head1)
    current = reversed_head1
    while current:
        print(current.val, end=" ")  # Output: 5 4 3 2 1
        current = current.next
    print()

    # Test case 2: Reversing a single node list
    head2 = ListNode(1)
    
    reversed_head2 = Solution().reverseList(head2)
    print(reversed_head2.val)  # Output: 1

    # Test case 3: Reversing an empty list
    head3 = None
    
    reversed_head3 = Solution().reverseList(head3)
    print(reversed_head3)  # Output: None
    
    # Test case 4: Reversing a list of two nodes
    head4 = ListNode(1)
    head4.next = ListNode(2)
    reversed_head4 = Solution().reverseList(head4)
    current = reversed_head4
    while current:
        print(current.val, end=" ")  # Output: 2 1
        current = current.next
    print()

