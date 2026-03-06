from typing import List

def moveZeroes(nums: List[int]) -> None:

    if not nums:
        return 

    pos = 0
    
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos],nums[i] = nums[i],nums[pos]
            pos += 1
    
    
# Example Usage
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)