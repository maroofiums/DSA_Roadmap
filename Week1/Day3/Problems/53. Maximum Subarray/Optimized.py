from typing import List
# Kadane’s Algorithm
## Complexity:
## Time: O(n) 
## Space: O(1) 
def maxSubArray(nums: List[int]) -> int:
    max_sum = nums[0]
    curr_sum = nums[0]

    for num in nums:
        curr_sum = max(num,curr_sum + num)
        max_sum = max(max_sum,curr_sum)

    return max_sum

# Example Usage
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))