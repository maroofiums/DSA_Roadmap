from typing import List

def minEatingSpeed(piles: List[int], h: int) -> int:
    low, high = 1, max(piles)

    while low < high:
        mid = low + ((high - low) // 2)

        hours = 0
        for pile in piles:
            hours += (pile + mid - 1) // mid
            
        if hours <= h:
            high = mid
        else:
            low = mid + 1
    return low

# Example Usage
piles = [3,6,7,11]
h = 8
print(minEatingSpeed(piles, h))  # Output: 4