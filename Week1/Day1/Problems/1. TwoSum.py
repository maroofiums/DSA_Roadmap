from typing import List

def TwoSum(nums:List[int],target:int) -> List[int]:
    seen = {}

    for i in range(len(nums)):
        required = target - nums[i]

        if required in seen:
            return [seen[required], i]
        
        seen[nums[i]] = i
    
    return None

# Example Usage

nums = [2, 7, 11, 15]
target = 9

result = TwoSum(nums, target)
print(result)
if result and nums[result[0]] + nums[result[1]] == target:
    print("Working Fine.........")