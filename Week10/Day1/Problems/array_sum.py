from typing import List

def array_sum(nums: List[int],i = 0) -> int:
    if i == len(nums):
        return 0
    return nums[i] + array_sum(nums,i + 1)
nums: List[int] = [1,2,3,4]
print(array_sum(nums))