# Brute Force Solution (O(n²) time)
## Check every possible pair of buy and sell days:
from typing import List

def maxProfit(prices: List[int]) -> int:
    max_profit = 0

    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
    
    return max_profit


# Example Usage
prices = [7,1,5,3,6,4] # -> Output: 5
print(maxProfit(prices))
