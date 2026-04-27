from typing import List

def searchRange(nums: List[int], target: int) -> List[int]:
    def lower_bound(x: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < x:
                left = mid + 1
            else:
                right = mid
        return left
    
    first = lower_bound(target)
    last = lower_bound(target + 1) - 1

    if first == len(nums) or nums[first] != target:
        return [-1, -1] 
    return [first, last]

# Example usage:
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(searchRange(nums, target))  # Output: [3, 4]