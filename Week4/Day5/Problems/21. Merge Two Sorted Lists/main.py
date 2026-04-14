class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2

        return dummy.next

    def traverse(self):
        current = self
        while current:
            print(current.val, end=' -> ')
            current = current.next
        print('None')

# Example usage:
# Create first sorted linked list: 1 -> 2 -> 4 -> None
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)
# Create second sorted linked list: 1 -> 3 -> 4 -> None
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)
# Merge the two lists
merged_list = ListNode().mergeTwoLists(list1, list2)
# Print merged list
merged_list.traverse()  # Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None
