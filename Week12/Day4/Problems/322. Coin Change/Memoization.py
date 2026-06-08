from typing import List

def coinChange(coins: List[int], amount:int) ->  int:

    memo = {}

    def dfs(x):
        if x == 0:
            return 0
        
        if x < 0:
            return float('inf')
        
        if x in memo:
            return memo[x]

        ans = float('inf')

        for coin in coins:
            ans = min(
                ans,
                1 + dfs(x-coin)
            )
        
        memo[x] = ans
        return ans

    res = dfs(amount)

    return res if res != float('inf') else -1

coins: List[int] = [1,2,5]
amount: int = 11

print(coinChange(coins,amount))