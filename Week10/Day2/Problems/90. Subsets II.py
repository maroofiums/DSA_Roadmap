from typing import List

def subsetsWithDup(nums:List[int]) -> List[List[int]]:
    res = []
    subset = []
    n = len(nums)

    def backtrack(i):
        if i >= n:
            res.append(subset[:])
            return
        
        subset.append(nums[i])
        backtrack(i+1)
        subset.pop()
        while i+1 < n and nums[i] == nums[i+1]:
            i += 1
        backtrack(i+1)

    backtrack(0)

    return res

if __name__ == "__main__":
    nums: List[int] = [1,2,3]
    print(subsetsWithDup(nums))