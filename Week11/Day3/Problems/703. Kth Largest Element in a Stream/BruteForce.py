from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)

        self.nums.sort()

        return self.nums[-self.k]
    

# Example Usage

kthLargest = KthLargest(3, [4, 5, 8, 2])

print(kthLargest.add(3))   # 4
print(kthLargest.add(5))   # 5
print(kthLargest.add(10))  # 5
print(kthLargest.add(9))   # 8
print(kthLargest.add(4))   # 8