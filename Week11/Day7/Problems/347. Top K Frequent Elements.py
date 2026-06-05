import heapq
from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = {}

    for num in nums:
        count[num] = count.get(num,0) + 1
    heap = []


    for num,count in count.items():
        heapq.heappush(heap,(count,num))

        if len(heap) > k:
            heapq.heappop(heap)

    return [num for count,num in heap]

nums: List[int] = [1,1,1,2,2,3]
k: int = 2

print(topKFrequent(nums,k))