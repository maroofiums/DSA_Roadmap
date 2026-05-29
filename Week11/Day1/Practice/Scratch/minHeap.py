class MinHeap:
    def __init__(self):
        self.heap = []

    def left(self,i):
        return 2 * i + 1
    
    def right(self,i):
        return 2 * i + 2
    
    def parent(self,i):
        return (i - 1) // 2
    

    def push(self,val):
        self.heap.append(val)

        i = len(self.heap) - 1

        while i > 0:
            p = self.parent(i)

            if self.heap[p] <= self.heap[i]:
                break

            self.heap[p],self.heap[i] = self.heap[i],self.heap[p]

            i = p

    def peek(self):
        if not self.heap:
            return None
        
        return self.heap[0]
    
    def pop(self):

        if not self.heap:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0] 
        self.heap[0] = self.heap.pop()

        i = 0
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
        
        return root

    def heap_sort(self,arr):
        for x in arr:
            self.push(x)

        res = []
        while self.heap:
            res.append(self.pop())

        return res
    
if __name__ == "__main__":
    # Create heap
    h = MinHeap()

    # Insert values
    h.push(10)
    h.push(4)
    h.push(15)
    h.push(1)
    h.push(7)

    print(h.heap)
    # Example internal heap structure:
    # [1, 4, 15, 10, 7]

    # Peek smallest element
    print(h.peek())
    # 1

    # Remove smallest element
    print(h.pop())
    # 1

    print(h.heap)
    # [4, 7, 15, 10]

    print(h.pop())
    # 4

    print(h.heap)
    # [7, 10, 15]

    # Heap sort example
    arr = [9, 3, 6, 1, 8, 2]

    sorted_arr = h.heap_sort(arr)

    print(sorted_arr)
    # [1, 2, 3, 6, 8, 9]