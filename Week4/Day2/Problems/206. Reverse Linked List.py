class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

def reverseList(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

def traverse(head):
    while head:
        print(head.value, end=" => ")
        head = head.next
    print("None")

if __name__ == "__main__":
    print("Original list:")
    traverse(head)
    reversed_head = reverseList(head)
    print("Reversed list:")
    traverse(reversed_head)