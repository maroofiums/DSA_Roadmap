from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        l = i + 1
        r = len(nums) -1

        while l < r:
            sumOfThree = nums[i] + nums[l] + nums[r]

            if sumOfThree == 0:
                res.append([nums[i],nums[l],nums[r]])
                while l < r and nums[r] == nums[r-1]:
                    r-=1
                while l < r and nums[l] == nums[l+1]:
                    l+=1
                
                l+=1
                r-=1 
            elif sumOfThree > 0:
                r -= 1
            else:
                l +=1
    return res

# Example Usage
nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))