from typing import List
from collections import defaultdict

def subarraySum(nums: List[int], k: int) -> int:
    prefix_map = defaultdict(int)
    prefix_map[0] = 1

    count = 0
    curr_sum = 0

    for num in nums:
        curr_sum += num

        if (curr_sum - k) in prefix_map:
            count += prefix_map[curr_sum - k]

        prefix_map[curr_sum] += 1

    return count

# Example Usage

nums = [1,1,1]
k = 2

print(subarraySum(nums,k))