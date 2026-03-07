from typing import List

def MaxProfit(prices:List[int])->int:
    if not prices:
        return 0
    
    max_profit = 0
    min_price = prices[0]

    for price in prices[1:]:
        profit = price - min_price

        if max_profit < profit:
            max_profit = profit
        if min_price > price:
            min_price = price
        
    return max_profit


# Example usage
prices = [7,1,5,3,6,4]
print(MaxProfit(prices))  # Output: 5
