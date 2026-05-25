from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    sol = []
    res =[]

    def backtrack():
        if len(nums) == len(sol):
            res.append(sol[:])
            return
        for x in nums:  
            if x not in sol:
                sol.append(x)
                backtrack()
                sol.pop()

    backtrack()
    return res 

nums: List[int] = [1,2,3]
print(permute(nums))