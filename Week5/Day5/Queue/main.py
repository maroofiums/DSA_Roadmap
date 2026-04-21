from typing import List

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self,value):
        self.items.append(value)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0 
    
    def size(self):
        return len(self.items)
    
    def display(self):
        print(self.items)

# Example Usage: 
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()
# [10, 20, 30]

print(q.dequeue())   # 10
print(q.front())     # 20
print(q.size())      # 2