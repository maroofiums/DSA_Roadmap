class MaxHeap:
    def __init__(self):
        self.heap = []

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def parent(self, i):
        return (i - 1) // 2

    def push(self, val):
        self.heap.append(val)

        i = len(self.heap) - 1

        while i > 0:
            p = self.parent(i)

            if self.heap[p] >= self.heap[i]:
                break

            self.heap[p], self.heap[i] = self.heap[i], self.heap[p]

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

            larger = i

            l = self.left(i)
            r = self.right(i)

            if l < n and self.heap[l] > self.heap[larger]:
                larger = l

            if r < n and self.heap[r] > self.heap[larger]:
                larger = r

            if larger == i:
                break

            self.heap[i], self.heap[larger] = self.heap[larger], self.heap[i]

            i = larger

        return root

    def heap_sort(self, arr):

        for x in arr:
            self.push(x)

        res = []

        while self.heap:
            res.append(self.pop())

        return res


if __name__ == "__main__":

    h = MaxHeap()

    h.push(10)
    h.push(4)
    h.push(15)
    h.push(1)
    h.push(7)

    print(h.heap)
    # Example:
    # [15, 7, 10, 1, 4]

    print(h.peek())
    # 15

    print(h.pop())
    # 15

    print(h.heap)

    arr = [9, 3, 6, 1, 8, 2]

    sorted_arr = h.heap_sort(arr)

    print(sorted_arr)
    # [9, 8, 6, 3, 2, 1]