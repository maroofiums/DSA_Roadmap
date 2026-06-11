from typing import List

def lengthOfLIS(nums: List[int]) -> int:

    n = len(nums)

    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(
                    dp[i],
                    dp[j] + 1
               )

    return max(dp)

nums: List[int] = [10,9,2,5,3,7,101,18]

print(lengthOfLIS(nums))