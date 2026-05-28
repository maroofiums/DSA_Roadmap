from typing import List

def partition(s: str) -> List[List[str]]:
    def isPalindrome(string):
        l = 0
        r = len(string) - 1

        while l < r:
            if string[l] != string[r]:
                return False
            
            l += 1
            r -= 1
        return True
    
    res,path = [],[]

    def backtrack(start):
        if start == len(s):
            res.append(path[:])
            return
        


        for end in range(start+1,len(s)+1):
            substring = s[start:end]

            if isPalindrome(substring):
                path.append(substring)    
                backtrack(end)
                path.pop()    

    backtrack(0)
    return res

s:str = "aab"
print(partition(s))