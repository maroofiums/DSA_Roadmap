from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    res = []

    def  backtrack(path):
        if len(path) == len(nums):
            res.append(path[:])
            return 

        for num in nums:
            if num in path:
                continue
                
            path.append(num)
            backtrack(path)
            path.pop()

    backtrack([])
    return res

nums:List[int] = [1,2,3]
print(permute(nums))