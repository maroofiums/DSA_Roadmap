def combination(candidates,target):
    res = []
    
    def backtrack(i,curr,total):
        if total == target:
            res.append(curr[:])
            return
        
        if i >= len(candidates) or target < total:
            return
        
        curr.append(candidates[i])
        backtrack(i,curr,total + candidates[i])
        curr.pop()
        backtrack(i+1,curr,total)
    
    backtrack(0,[],0)
    return res
target = 7
nums = [2,3,6,7]

print(combination(nums,target))