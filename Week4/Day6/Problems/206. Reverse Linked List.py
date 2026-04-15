class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 

    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head

        while current:
            next_node = current.next  # Store the next node
            current.next = prev       # Reverse the current node's pointer
            prev = current            # Move prev to the current node
            current = next_node       # Move to the next node

        return prev  # At the end, prev will be the new head of the reversed list
    
    def create(self,arr):
        head = ListNode(arr[0])
        current = head
        for i in range(1, len(arr)):
            current.next = ListNode(arr[i])
            current = current.next
        return head

    def printList(self, head):
        current = head
        while current:
            print(current.val, end=' -> ')
            current = current.next
        print("None")

# Example usage:
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    list_node = ListNode()
    head = list_node.create(arr)
    print("Original list:")
    list_node.printList(head)

    reversed_head = list_node.reverseList(head)
    print("Reversed list:")
    list_node.printList(reversed_head)
    