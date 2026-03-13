class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
# Test cases
if __name__ == "__main__":
    # Test case 1: No cycle
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(3)
    print(Solution().hasCycle(head1))  # Output: False

    # Test case 2: Cycle exists
    head2 = ListNode(1)
    head2.next = ListNode(2)
    head2.next.next = ListNode(3)
    head2.next.next.next = head2  # Creates a cycle
    print(Solution().hasCycle(head2))  # Output: True

    # Test case 3: Single node with no cycle
    head3 = ListNode(1)
    print(Solution().hasCycle(head3))  # Output: False

    # Test case 4: Single node with a cycle
    head4 = ListNode(1)
    head4.next = head4  # Creates a cycle
    print(Solution().hasCycle(head4))  # Output: True