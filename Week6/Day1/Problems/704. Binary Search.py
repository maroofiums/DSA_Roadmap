from typing import List

def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    return -1

# Example usage:
find = search([-1,0,3,5,9,12], 9)  # Output: 4
print(find)