from typing import List

def maxProfit(prices: List[int]) -> int:
    max_profit = 0
    min_price = prices[0]

    for price in prices[1:]:
        profit = price - min_price

        min_price = min(min_price,price)
        max_profit = max(max_profit,profit)

    return max_profit

# Example Usage
prices: List[int] = [7,1,5,3,6,4]

print(maxProfit(prices))