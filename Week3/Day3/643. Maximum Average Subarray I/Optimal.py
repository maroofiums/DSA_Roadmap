from typing import List

def findAverage(nums: List[int], k: int) -> float:
    curr_sum = sum(nums[:k])
    max_sum = curr_sum

    for i in range(k, len(nums)):
        curr_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, curr_sum)
    return max_sum / k

# Example usage:
nums: List[int] = [1, 12, -5, -6, 50, 3]
k: int = 4
print(findAverage(nums, k))  # Output: 12.75