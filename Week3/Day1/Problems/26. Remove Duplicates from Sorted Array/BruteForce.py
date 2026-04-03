def removeDuplicates(nums):
    unique= sorted(set(nums))
    for i in range(len(unique)):
        nums[i]=unique[i]
    return len(unique)
# Example usage:
nums = [1, 1, 2]
new_length = removeDuplicates(nums)
print("New length:", new_length)
print("Modified array:", nums[:new_length])

## Complexity
# Time Complexity: O(n log n) due to the sorting step.
# Space Complexity: O(n) because of the additional space used to store the unique elements in