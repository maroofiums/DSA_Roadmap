from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    res = []
    sol = []

    def backtrack(i = 0):
        if i >= len(nums):
            res.append(sol[:])
            return
        
        backtrack(i+1)
        sol.append(nums[i])
        backtrack(i+1)
        sol.pop()

    backtrack()

    return res

nums: List[int] = [1,2,3]
print(subsets(nums))

