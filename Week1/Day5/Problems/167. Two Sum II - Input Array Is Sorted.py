from typing import List

def twoSum(nums:List[int],target:int) -> List[int]:
    l = 0
    r = len(nums) - 1

    while l < r:
        sumOfTwo = nums[l] +nums[r]
        if sumOfTwo == target:
            return [l+1,r+1]
        
        elif sumOfTwo > target:
            r -=1 
        else: 
            l += 1

    return []

# Example Usage 
nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))