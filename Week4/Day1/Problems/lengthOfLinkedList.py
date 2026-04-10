class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node(1)
second = Node(2)
third = Node(3)
tail = Node(4)

head.next = second
second.next = third
third.next = tail

def lengthOfLinkedList(head):
    count = 0
    curr = head

    while curr:
        count += 1
        curr = curr.next

    return count

if __name__ == "__main__":
    len = lengthOfLinkedList(head)
    print(len)