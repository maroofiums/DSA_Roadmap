def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    write = 0

    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write],nums[read] = nums[read],nums[write]
            write += 1
    
# Example usage:
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]

    
