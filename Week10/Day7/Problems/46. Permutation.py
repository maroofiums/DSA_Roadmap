def permute(nums):
    res,path = [],[]

    def backtrack():
        if len(path) == len(nums):
            res.append(path[:])
            return
        
        for num in nums:
            if num in path:
                continue
            path.append(num)
            backtrack()
            path.pop()
    backtrack()
    return res

nums = [1,2,3]

print(permute(nums))