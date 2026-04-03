def removeElement(nums, val):
    temp = []

    for x in nums:
        if x != val:
            temp.append(x)

    # copy back
    for i in range(len(temp)):
        nums[i] = temp[i]

    return len(temp)

# Example Usage
nums = [3, 2, 2, 3]
val = 3
new_length = removeElement(nums, val)
print("New length:", new_length)
print("Modified array:", nums[:new_length])
## Complexity
# Time Complexity: O(n) because we traverse the array once to filter out the elements.
# Space Complexity: O(n) because of the additional space used to store the filtered elements in the temp list.