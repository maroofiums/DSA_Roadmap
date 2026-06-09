from typing import List

def lengthOfLIS(nums: List[int]) -> int:

    n = len(nums)

    memo = {}

    def dfs(i, prev):

        if i == n:
            return 0

        if (i, prev) in memo:
            return memo[(i, prev)]

        skip = dfs(i + 1, prev)

        take = 0

        if prev == -1 or nums[i] > nums[prev]:
            take = 1 + dfs(i + 1, i)

        memo[(i, prev)] = max(take, skip)

        return memo[(i, prev)]

    return dfs(0, -1)

nums: List[int] = [10,9,2,5,3,7,101,18]

print(lengthOfLIS(nums))