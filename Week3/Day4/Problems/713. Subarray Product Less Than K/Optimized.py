from typing import List

def numSubarrayProductLessThenK(nums: List[int],k:int) -> int:
    product = 1
    l = count = 0

    for r in range(len(nums)):
        product *= nums[r]
        while product >= k:
            product //= nums[l]
            l += 1
        count += (r - l + 1)
    
    return count

# Example Usage
nums: List[int] = [10,5,2,6]
k: int = 100

print(numSubarrayProductLessThenK(nums=nums,k=k))