from typing import List

def minCostClimbingStrairs(cost: List[int]) -> int:
    n = len(cost)

    dp = [0] * (n+1)
    dp[0],dp[1] = 0,0

    for i in range(2,n+1):
        dp[i] = min(
            cost[i-1] + dp[i-1],
            cost[i-2] + dp[i-2],
        )
        
        return dp[i]
    
    return dp[n]

cost: List[int] = [10,15,20]

print(minCostClimbingStrairs(cost))