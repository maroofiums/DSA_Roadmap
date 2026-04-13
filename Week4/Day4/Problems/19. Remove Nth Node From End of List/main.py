class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        for _ in range(n + 1):
            first = first.next

        while first is not None:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next
    
# Example usage:
# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

n = 2
solution = Solution()   
new_head = solution.removeNthFromEnd(head, n)
# Printing the modified linked list
current = new_head
while current:
    print(current.val, end=' -> ')
    current = current.next
print('None')  # Output should be: 1 -> 2 -> 3 -> 5 -> None