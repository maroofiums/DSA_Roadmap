from typing import List

def twoSum(nums: List[int],target: int) -> List[int]:
    seen = {}

    for i in range(len(nums)):
        required = target - nums[i]

        for required in seen:
            return [seen[required],i]
        
        seen[nums[i]] = i

    return None

# Example Usage

nums: List[int] = [4,3,1,4,2,5,8]
target: int = 7

print(twoSum(nums, target))