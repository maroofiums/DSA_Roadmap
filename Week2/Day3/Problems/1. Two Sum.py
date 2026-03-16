from typing import List

def twoSum(nums: List[int],target: int) -> List[int]:
    seen = {}

    for i in range(len(nums)):
        required = target - nums[i]

        if required in seen:
            return [seen[required],i]
        
        seen[nums[i]] = i

    return []

# Example Usage

nums: List[int] = [2,7,11,15]
target: int = 9

print(twoSum(nums,target))