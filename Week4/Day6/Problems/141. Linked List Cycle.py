class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 

    def hasCycle(self, head):
        if not head:
            return False

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
    
    def create(self, arr):
        if not arr:
            return None

        head = ListNode(arr[0])
        current = head

        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next

        return head

    def traverse(self, head):
        current = head
        while current:
            print(current.val, end=' -> ')
            current = current.next
        print('None')

# Example usage:
if __name__ == "__main__":
    linked_list = ListNode()
    head = linked_list.create([3, 2, 0, -4])
    # Creating a cycle for testing
    head.next.next.next.next = head.next

    print(linked_list.hasCycle(head))  # Output: True
    head_no_cycle = linked_list.create([1, 2, 3, 4])
    print(linked_list.hasCycle(head_no_cycle))  # Output: False
    