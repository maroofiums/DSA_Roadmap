from typing import List

def coinChange(coins: List[int], amount: int) -> int:

    dp = [float('inf')] * (amount + 1)

    dp[0] = 0

    for x in range(1,amount+1):
        for coin in coins:
            if x - coin >= 0:
                dp[x] = min(
                    dp[x],
                    dp[x-coin] + 1
                )

    return dp[amount] if dp[amount] != float("inf") else -1 

coins: List[int] = [1,2,5]
amount: int = 11

print(coinChange(coins, amount))