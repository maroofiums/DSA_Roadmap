from typing import List

def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    m, n = len(obstacleGrid), len(obstacleGrid[0])

    def dfs(i,j):
        if i >= m or j >= n:
            return 0

        if obstacleGrid[i][j] == 1:
            return 0

        if i == m - 1 and j == n - 1:
            return 1
            
        down = dfs(i+1,j)
        right = dfs(i,j+1)

        return down + right
            
    return dfs(0,0)

obstacleGrid: List[List[int]] = [
                                    [0,0,0],
                                    [0,1,0],
                                    [0,0,0]
                                ]

print(uniquePathsWithObstacles(obstacleGrid))