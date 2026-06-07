from typing import List

def rob(nums: List[int]) -> int:
    n = len(nums)

    def helper(i):
        if i == 0:
            return nums[0]

        if i == 1:
            return max(nums[0],nums[1])

        return max(
            nums[i]+helper(i-2),
            helper(i-1)
        )

    return helper(n-1)

nums: List[int] = [2,7,9,3,1]
print(rob(nums))