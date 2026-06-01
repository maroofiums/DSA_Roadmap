from typing import List,Counter

def topKFrequent(nums, k):
    freq = Counter(nums)

    sorted_nums = sorted(
        freq.keys(),
        key=lambda x: freq[x],
        reverse=True
    )

    return sorted_nums[:k]

# Example Usage:

nums: List[int] = [1,1,1,2,2,3]
k: int = 2

print(topKFrequent(nums, k))