from typing import List

def maxProfit(prices: List[int]) -> int:
    n = len(prices)

    def dfs(i,holding,buy_price):
        if i == n:
            return 0
        
        if holding:
            return max(dfs(i+1,True,buy_price),dfs(i+1,False,0)+prices[i]-buy_price)
        else:
            return max(dfs(i+1,False,0),dfs(i+1,True,prices[i]))
        
    return dfs(0,False,0)

prices: List[int] = [7,1,5,3,6,4]
print(maxProfit(prices))