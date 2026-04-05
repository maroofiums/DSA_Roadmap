from typing import List

def findAverage(nums: List[int], k: int) -> float:
    max_average = float('-inf')
    for i in range(len(nums) - k + 1):
        current_sum = sum(nums[i:i+k])
        current_average = current_sum / k
        max_average = max(max_average, current_average)
    return max_average

# Example usage:
nums: List[int] = [1, 12, -5, -6, 50, 3]
k: int = 4

print(findAverage(nums, k))  # Output: 12.75