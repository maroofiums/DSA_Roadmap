from typing import List

def minCostClimbingStrairs(cost: List[int]) -> int:
    n = len(cost)

    memo = {0:0,1:0}

    def min_cost(i):
        if i in memo:
            return memo[i]
        else:
            memo[i] = min(
                cost[i-1] + min_cost(i-1),
                cost[i-2] + min_cost(i-2),
            )
        
        return memo[i]
    
    return min_cost(n)

cost: List[int] = [10,15,20]

print(minCostClimbingStrairs(cost))