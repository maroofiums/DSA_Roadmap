from typing import List

def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    zero_count = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            nums[zero_count], nums[i] = nums[i], nums[zero_count]
            zero_count += 1

# Example usage:
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]