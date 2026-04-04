from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
    return []

# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Example usage:
print(twoSum([2, 7, 11, 15], 9))  # Output: [1, 2]