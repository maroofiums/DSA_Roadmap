# Optimal Solution (O(n) time)
## Keep track of:
### min_price → lowest price seen so far
### max_profit → maximum profit possible by selling at the current price

from typing import List

def maxProfit(prices: List[int]) -> int:
    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        profit = price - min_price

        min_price = min(min_price,price)
        max_profit = max(max_profit,profit)

    return max_profit

# Example Usage
prices = [7,1,5,3,6,4] # -> Output: 5

print(maxProfit(prices))