from typing import List
import heapq

def findKthLargest(nums: List[int], k: int) -> int:
    heap = []

    for num in nums:
        heapq.heappush(heap,num)
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]

nums: List[int] = [3,2,1,5,6,4]
k: int = 2

print(findKthLargest(nums,k))