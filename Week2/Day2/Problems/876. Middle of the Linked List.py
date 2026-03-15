from typing import Optional

class ListNode:
    def __init__(self,val = 0,next = None):
        self.val = val 
        self.next = next


class Solution:
    def middleNode(self,head: Optional[ListNode]):

        slow = head.next 
        fast = head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
    

# Example Usage 

# Creating linked list: 1 → 2 → 3 → 4 → 5

n5 = ListNode(5)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)

solution = Solution()
middle = solution.middleNode(n1)

print(middle.val)