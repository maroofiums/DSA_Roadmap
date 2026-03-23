from typing import List
# Brute Force
# # Complexity:
# # Time: O(n²)
# # Space: O(1)
def maxSubArray(nums:List[int]) -> int:
    n = len(nums)
    max_sum = float('-inf')
    
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            max_sum = max(max_sum, current_sum)
    
    return max_sum

# Example Usage
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))