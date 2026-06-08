from typing import List

def coinChange(coins: List[int], amount:int) ->  int:

    def dfs(i, x):
        if x == 0:
            return 1
        
        if x < 0:
            return 0

        if i == len(coins):
            return 0

        take = dfs(i,x - coins[i])
        skip = dfs(i+1,x)
        
        return skip + take

    return dfs(0, amount)


coins: List[int] = [1,2,5]
amount: int = 5

print(coinChange(coins,amount))