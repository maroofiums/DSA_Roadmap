from typing import List

def maxSubArray(nums: List[int]) -> int:
    max_sum = nums[0]
    curr = nums[0]
    for num in nums[1:]:
        curr = max(num , curr + num)
        max_sum = max(max_sum,curr)

    return max_sum

# Example Usage
nums: List[int] = [-2,1,-3,4,-1,2,1,-5,4]

print(maxSubArray(nums))