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
    
    def hasCycle(self) -> bool:
        slow = self
        fast = self

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

# Example usage:
arr = [3, 2, 0, -4]
list_node = ListNode().create(arr)
# Create a cycle for testing
list_node.next.next.next.next = list_node.next
print("Does the linked list have a cycle?", list_node.hasCycle())
