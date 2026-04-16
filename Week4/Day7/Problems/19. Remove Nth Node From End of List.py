from typing import List

class ListNode:
    def __init__(self, val = 0,next = None):
        self.val = val
        self.next = next
    
    def traverse(self):
        current = self
        while current:
            print(current.val,end=" -> ")
            current = current.next
        print("None")

    def create(self,arr:List[int]):
        head = ListNode(arr[0])
        current = head
        for i in range(1,len(arr)):
            current.next = ListNode(arr[i])
            current = current.next
        return head
    
    def removeNthFromEnd(self, n: int) -> 'ListNode':
        dummy = ListNode(0)
        dummy.next = self
        first = dummy
        second = dummy

        for _ in range(n + 1):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next
    
# Example usage:
# Create a linked list from an array
arr = [1, 2, 3, 4, 5]
list_node = ListNode().create(arr)
print("Original list:")
list_node.traverse()
# Remove the 2nd node from the end
n = 2
new_head = list_node.removeNthFromEnd(n)
print(f"List after removing {n}th node from the end:")
new_head.traverse()
