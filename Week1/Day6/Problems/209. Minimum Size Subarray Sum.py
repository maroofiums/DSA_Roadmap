from typing import List

def minSubArrayLen(nums: List[int], target: int) -> int:
    l = total = 0
    min_len = len(nums) + 1

    for r in range(len(nums)):
        total += nums[r]
        while total >= target:
            min_len = min(min_len,r-l+1)
            total -= nums[l]
            l += 1
        
    
    return 0 if min_len == len(nums) + 1 else min_len

# Example Usage
nums: List[int] = [2,3,1,2,4,3]
target: int = 7

print(minSubArrayLen(nums,target))