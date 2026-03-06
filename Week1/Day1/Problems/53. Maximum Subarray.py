from typing import List 
import pytest
    
def maximumSubarray(nums: List[int]) -> int:
    if not nums:
        return 0

    curr_sum: int = nums[0]
    max_sum: int = nums[0]

    for i in range(1,len(nums)):
        curr_sum = max(nums[i],curr_sum + nums[i])
        max_sum = max(max_sum,curr_sum)
    
    return max_sum

# Example Usage

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

max_sub = maximumSubarray(arr)

print(f"Maximum Sum of Subarray id: {max_sub}")
