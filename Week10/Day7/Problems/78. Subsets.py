from typing import List

def subsets(nums: List[List[int]]) -> List[List[int]]:

    res,path = [],[]

    def backtrack(idx):
        res.append(path[:])

        for i in range(idx,len(nums)):
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()
        
    backtrack(0)

    return res

nums: List[List[int]] = [1,2,3]

print(subsets(nums))

