from typing import List

def maxArea(heights: List[int]) -> int:
    l,r = 0,len(heights) - 1
    area = max_area = 0

    while l < r:
        area = (r - l) * min(heights[l], heights[r])
        max_area = max(area, max_area)

        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1
    return max_area

# Example usage:
heights = [1,8,6,2,5,4,8,3,7]
print(maxArea(heights))  # Output: 49
