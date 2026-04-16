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
    
    def reverseList(self) -> 'ListNode':
        prev = None
        current = self

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev
    
# Example usage:
arr = [1, 2, 3, 4, 5]
list_node = ListNode().create(arr)
print("Original list:")
list_node.traverse()
reversed_head = list_node.reverseList()
print("Reversed list:")
reversed_head.traverse()
