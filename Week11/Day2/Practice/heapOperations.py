class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self,i):
        return (i-1) // 2
    
    def left(self,i):
        return 2 * i + 1
    
    def right(self,i):
        return 2 * i + 2
    
    def shift_down(self,i):
        n = len(self.heap)

        while True:
            smaller = i

            l = self.left(i)
            r = self.right(i)

            if l < n and self.heap[l] < self.heap[smaller]:
                smaller = l
           
            if r < n and self.heap[r] < self.heap[smaller]:
                smaller = r

            if smaller == i:
                break

            self.heap[i],self.heap[smaller] = self.heap[smaller],self.heap[i]

            i = smaller
    
    def shift_up(self,i):
        while i > 0:
            p = self.parent(i)

            if self.heap[p] <= self.heap[i]:
                break
            
            self.heap[p],self.heap[i] = self.heap[i],self.heap[p]

            i = p

    def push(self,val):
        self.heap.append(val)
        self.shift_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]

        self.heap[0] = self.heap.pop()

        self.shift_down(0)

        return root
    

    def heapify(self,arr):
        self.heap = arr[:]

        start = len(self.heap) // 2 - 1

        for i in range(start,-1,-1):
            self.shift_down(i)

    def size(self):
        return len(self.heap)
    
    def is_empty(self):
        return self.size() == 0
    
    def display(self):
        print(self.heap)


if __name__ == "__main__":
    h = MinHeap()

    h.push(5)
    h.push(3)
    h.push(8)
    h.push(1)

    h.display()

    print(h.pop())  # 1
    print(h.pop())  # 3
    print(h.pop())  # 5
    print(h.pop())  # 8