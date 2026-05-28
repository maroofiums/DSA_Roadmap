from typing import List

def subsets(nums:List[int]) -> List[List[int]]:
    res,path = [],[]

    def backtrack(idx = 0):
        res.append(path[:])

        for i in range(idx,len(nums)):

            path.append(nums[i])
            backtrack(i+1)
            path.pop()

    
    backtrack()
    return res

nums: List[int] = [1,2,3]

print(subsets(nums))