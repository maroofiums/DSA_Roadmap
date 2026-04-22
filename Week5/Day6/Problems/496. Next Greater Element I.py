from typing import List

def nextGreaterElement(nums1: List[int],nums2: List[int]) -> List[int]:
    stack = []
    nextGreater = {}

    for num in nums2:
        while stack and num > stack[-1]:
            smaller = stack.pop()
            nextGreater[smaller] = num
        stack.append(num)

    while stack:
        nextGreater[stack.pop()] = -1

    return [nextGreater[n] for n in nums1]

# Example Usage:

nums1: List[int] = [4,1,2]
nums2: List[int] = [1,3,4,2]

print(nextGreaterElement(nums1,nums2))