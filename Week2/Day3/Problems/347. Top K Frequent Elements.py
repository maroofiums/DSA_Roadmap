from collections import Counter
from typing import List
import heapq


def topKFrequent(nums: List[int],k: int) -> List[int]:
    freq = Counter(nums)
    heap = []

    for num, count in freq.items():
        heapq.heappush(heap,(count,num))

        if len(heap) > k:
            heapq.heappop(heap)

    return [num for count,num in heap]

# Example Usage

nums = [1,1,1,2,2,3]
k = 2

print(topKFrequent(nums,k))