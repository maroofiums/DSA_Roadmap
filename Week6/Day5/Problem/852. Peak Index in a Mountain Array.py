from typing import List

def peakIndexInMountainArray(arr: List[int]) -> int:
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left 

# Example usage:
arr: List[int] = [0, 1, 0]
print(peakIndexInMountainArray(arr))  # Output: 1