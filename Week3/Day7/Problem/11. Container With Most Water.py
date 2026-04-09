from typing import List

def maxArea(height: List[int]) -> int:
    l,r = 0, len(height)-1
    max_area = 0

    while l < r:
        min_height = min(height[l], height[r])
        width = r - l
        max_area = max(max_area, min_height * width)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_area

# Example usage:
height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))  # Output: 49


