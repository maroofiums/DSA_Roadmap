class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

first = Node(1)
second = Node(2)
third = Node(3)

first.next = second
second.next = third

def traverse(head):
    curr = head
    while curr:
        print(curr.value,end=" => ")
        curr = curr.next
    print("None")

if __name__ == "__main__":
    traverse(first)