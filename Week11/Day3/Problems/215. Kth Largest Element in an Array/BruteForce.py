from typing import List

def findKthLargest(nums: List[int], k: int) -> int:
    nums.sort()

    return nums[-k]

nums: List[int] = [3,2,1,5,6,4]
k: int = 2


print(findKthLargest(nums,k))