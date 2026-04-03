def removeElement(nums, val):
    write = 0
    for read in range(len(nums)):
        if nums[read] != val:
            nums[write] = nums[read]
            write += 1
    return write

# Example usage:
nums = [3, 2, 2, 3]
val = 3
new_length = removeElement(nums, val)
print(new_length)  # Output: 2
print(nums[:new_length])  # Output: [2, 2]

## Complexity Analysis:
# Time Complexity: O(n), where n is the length of the input array. We traverse
# the array once.
# Space Complexity: O(1), since we are modifying the array in place and using
# only a constant amount of extra space for the write pointer.