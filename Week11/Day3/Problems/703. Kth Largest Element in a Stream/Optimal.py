from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap,self.k = nums,k
        heapq.heapify(self.minHeap)

        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        
        heapq.heappush(self.minHeap,val)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]

# Example Usage

kthLargest = KthLargest(3, [4, 5, 8, 2])

print(kthLargest.add(3))   # 4
print(kthLargest.add(5))   # 5
print(kthLargest.add(10))  # 5
print(kthLargest.add(9))   # 8
print(kthLargest.add(4))   # 8