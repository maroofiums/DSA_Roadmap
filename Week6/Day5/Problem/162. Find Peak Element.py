from typing import List

def findPeakElement(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left

# Example usage:
nums: List[int] = [1, 2, 3, 1]
print(findPeakElement(nums))  # Output: 2