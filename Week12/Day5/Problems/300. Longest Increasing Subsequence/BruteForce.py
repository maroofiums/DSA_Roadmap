from typing import List

def lengthOfLIS(nums: List[int]) -> int:
    n = len(nums)

    def dfs(idx, prev):
        if idx == n:
            return 0

        # Skip current element
        skip = dfs(idx + 1, prev)

        # Take current element
        take = 0
        if prev == -1 or nums[idx] > nums[prev]:
            take = 1 + dfs(idx + 1, idx)

        return max(take, skip)

    return dfs(0, -1)

nums: List[int] = [10,9,2,5,3,7,101,18]

print(lengthOfLIS(nums))