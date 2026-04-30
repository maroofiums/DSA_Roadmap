from typing import List

def minEatingSpeed(piles: List[int], h: int) -> int:
    left, right = 1, max(piles)

    while left < right:
        mid = (left + right) // 2
        hours_needed = sum((pile + mid - 1) // mid for pile in piles)

        if hours_needed > h:
            left = mid + 1
        else:
            right = mid

    return left

# Example usage:
piles = [3, 6, 7, 11]
h = 8
print(minEatingSpeed(piles, h))  # Output: 4 (Koko can eat all bananas in 8 hours at speed 4)