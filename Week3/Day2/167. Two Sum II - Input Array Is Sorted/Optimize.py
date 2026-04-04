from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers) - 1
    while l < r:
        current_sum = numbers[l] + numbers[r]
        if current_sum == target:
            return [l + 1, r + 1]
        elif current_sum < target:
            l += 1
        else:
            r -= 1
    return []

# Time Complexity: O(n)
# Space Complexity: O(1)

# Example usage:
print(twoSum([2, 7, 11, 15], 9))  # Output: [1, 2]
