from typing import List

def minCostClimbingStrairs(cost: List[int]) -> int:
    n = len(cost)

    def min_cost(i):
        if i < 2:
            return 0
        
        return min(
            cost[i-1] + min_cost(i-1),
            cost[i-2] + min_cost(i-2),
        )
    
    return min_cost(n)

cost: List[int] = [10,15,20]

print(minCostClimbingStrairs(cost))