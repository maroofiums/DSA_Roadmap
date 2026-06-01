import heapq
from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:

    heap = []
    freq= {}

    for num in nums:
        freq[num] = freq.get(num,0) + 1

    for num,count in freq.items():
        heapq.heappush(heap,(count,num))

        if len(heap) > k:
            heapq.heappop(heap)

    return [num for count,num in heap]

# Example usage:
nums: List[int] = [1,1,1,2,2,3]
k: int = 2

print(topKFrequent(nums, k))