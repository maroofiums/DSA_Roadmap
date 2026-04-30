from typing import List

def shipWithinDays(weights: List[int], days: int) -> int:
    low, high = max(weights),sum(weights)

    while low < high:
        mid = low + ((high - low) // 2)

        D = 1 
        curr = 0

        for w in weights:
            if curr + w > mid:
                D += 1
                curr = 0
            curr += w
            
        if D <= days:
            high = mid
        else:
            low = mid + 1
    return low

# Example Usage
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
print(shipWithinDays(weights, days))  # Output: 15