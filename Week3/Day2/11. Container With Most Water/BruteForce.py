from typing import List

def maxArea(height: List[int]) -> int:
    max_area = 0
    n = len(height)
    
    for i in range(n):
        for j in range(i + 1, n):
            area = min(height[i], height[j]) * (j - i)
            max_area = max(max_area, area)
    
    return max_area
# Example usage:
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))  # Output: 49