from typing import List
# HashSet
## Complexity:
## Time: O(n) 
## Space: O(n) 
def maxSubArray(nums: List[int]) -> int:
    seen = set()
    
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    
    return False

# Example Usage
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))