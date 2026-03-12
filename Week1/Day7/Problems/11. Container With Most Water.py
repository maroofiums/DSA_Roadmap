from typing import List

def containMostWater(height: List[int]) -> int:
    l = 0
    r = len(height) - 1
    area = 0
    max_area = 0

    while l < r:
        width = r - l
        area = min(height[l],height[r]) * width
        max_area = max(max_area,area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    
    return max_area

# Example Usage

height: List[int] = [1,8,6,2,5,4,8,3,7]

print(containMostWater(height))