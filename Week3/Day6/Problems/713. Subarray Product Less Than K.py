from typing import List

def numSubarrayProductLessThank(nums: List[int],k: int) -> int:
    if k <= 0:
        return 0
    product = 1
    count, l = 0, 0
    for r in range(len(nums)):
        product *= nums[r]
        while product >= k:
            product /= nums[l]
            l += 1
        count += r - l + 1
    return count

# Example usage:
nums: List[int] = [10, 5, 2, 6]
k: int = 100
print(numSubarrayProductLessThank(nums, k))  # Output: 8
