def moveZeroes(nums):
    non_zero = []

    zero_count = 0

    for x in nums:
        if x != 0:
            non_zero.append(x)
        else:
            zero_count += 1

    non_zero.extend([0] * zero_count)

    for i in range(len(nums)):
        nums[i] = non_zero[i]

# Example usage:
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]