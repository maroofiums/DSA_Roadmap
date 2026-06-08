from typing import List

def coinChange(coins: List[int], amount:int) ->  int:

    dp = [0] * (amount + 1)

    dp[0] = 1

    for coin in coins:
        for x in range(coin,amount+1):
            dp[x] += dp[x - coin]


    return dp[amount]

coins: List[int] = [1,2,5]
amount: int = 4

print(coinChange(coins,amount))