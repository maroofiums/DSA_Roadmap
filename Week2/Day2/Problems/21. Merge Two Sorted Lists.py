from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 if list1 else list2
        return dummy.next

# Example Usage

# Creating list1: 1 -> 3 -> 5
l1 = ListNode(1, ListNode(3, ListNode(5)))

# Creating list2: 2 -> 4 -> 6
l2 = ListNode(2, ListNode(4, ListNode(6)))

solution = Solution()
merged_head = solution.mergeTwoLists(l1, l2)

# Print merged list
curr = merged_head
while curr:
    print(curr.val, end=" -> " if curr.next else "")
    curr = curr.next