from typing import List

def numSubarrayProductLessThanK(nums: List[int], k:int) -> int:
    n = len(nums)
    count = 0

    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= nums[j]
            if product < k:
                count += 1
            else:
                break   # optimization

    return count

# Example Usage
nums: List[int] = [10,5,2,6]
k: int = 100

print(numSubarrayProductLessThanK(nums=nums,k=k))