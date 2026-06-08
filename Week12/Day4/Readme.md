# Week 12 - Day 4: Coin Change Pattern

## Objective

Today you'll learn one of the most important DP patterns:

**Minimum Cost / Minimum Steps DP**

This pattern appears in:

* Coin Change
* Perfect Squares
* Minimum Path Sum
* Word Break
* Unbounded Knapsack

---

# Problem 1: Coin Change (LeetCode 322)

## Problem Statement

Given:

```python
coins = [1, 2, 5]
amount = 11
```

Find the minimum number of coins needed to make the amount.

Answer:

```python
11 = 5 + 5 + 1
```

Result:

```python
3
```

If impossible:

```python
return -1
```

---

# Why Greedy Fails

Consider:

```python
coins = [1, 3, 4]
amount = 6
```

Greedy:

```python
4 + 1 + 1 = 6
```

Uses:

```python
3 coins
```

Optimal:

```python
3 + 3 = 6
```

Uses:

```python
2 coins
```

Greedy chooses the locally best coin.

DP explores all possibilities and guarantees the global optimum.

---

# DP State

## Definition

```text
dp[x] = minimum coins needed to make amount x
```

Example:

```python
dp[7]
```

means:

```text
Minimum coins required to form amount 7
```

---

# Base Case

Amount 0 needs no coins.

```text
dp[0] = 0
```

---

# Transition

For every coin:

```text
dp[x] = min(
    dp[x],
    1 + dp[x - coin]
)
```

Meaning:

```text
Take one coin
+
best answer for remaining amount
```

---

# Example

```python
coins = [1,2,5]
amount = 5
```

Initial:

```python
dp = [0, inf, inf, inf, inf, inf]
```

Process coin = 1

```python
dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 4
dp[5] = 5
```

Process coin = 2

```python
dp[2] = 1
dp[3] = 2
dp[4] = 2
dp[5] = 3
```

Process coin = 5

```python
dp[5] = 1
```

Final:

```python
[0,1,1,2,2,1]
```

Answer:

```python
1
```

---

# Brute Force

```python
from typing import List

def coinChange(coins: List[int], amount: int) -> int:

    def dfs(rem):
        if rem == 0:
            return 0

        if rem < 0:
            return float("inf")

        ans = float("inf")

        for coin in coins:
            ans = min(
                ans,
                1 + dfs(rem - coin)
            )

        return ans

    result = dfs(amount)

    return result if result != float("inf") else -1
```

### Complexity

```text
Time: Exponential
Space: O(amount)
```

---

# Memoization

```python
from typing import List

def coinChange(coins: List[int], amount: int) -> int:

    memo = {}

    def dfs(rem):
        if rem == 0:
            return 0

        if rem < 0:
            return float("inf")

        if rem in memo:
            return memo[rem]

        ans = float("inf")

        for coin in coins:
            ans = min(
                ans,
                1 + dfs(rem - coin)
            )

        memo[rem] = ans
        return ans

    result = dfs(amount)

    return result if result != float("inf") else -1
```

### Complexity

```text
Time: O(amount × number_of_coins)
Space: O(amount)
```

---

# Tabulation

```python
from typing import List

def coinChange(coins: List[int], amount: int) -> int:

    dp = [float("inf")] * (amount + 1)

    dp[0] = 0

    for x in range(1, amount + 1):
        for coin in coins:
            if x - coin >= 0:
                dp[x] = min(
                    dp[x],
                    1 + dp[x - coin]
                )

    return dp[amount] if dp[amount] != float("inf") else -1
```

### Complexity

```text
Time: O(amount × number_of_coins)
Space: O(amount)
```

---

# Problem 2: Coin Change II (LeetCode 518)

## Difference from Coin Change

Coin Change:

```text
Find minimum number of coins
```

Coin Change II:

```text
Find total number of combinations
```

---

Example:

```python
coins = [1,2,5]
amount = 5
```

Ways:

```text
5

2 + 2 + 1

2 + 1 + 1 + 1

1 + 1 + 1 + 1 + 1
```

Answer:

```python
4
```

---

# DP State

```text
dp[x] = number of ways to make amount x
```

---

# Base Case

```text
dp[0] = 1
```

Why?

```text
There is exactly one way to make amount 0:
Choose nothing.
```

---

# Transition

```text
dp[x] += dp[x - coin]
```

---

# Tabulation

```python
from typing import List

def change(amount: int, coins: List[int]) -> int:

    dp = [0] * (amount + 1)

    dp[0] = 1

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] += dp[x - coin]

    return dp[amount]
```

### Complexity

```text
Time: O(amount × number_of_coins)
Space: O(amount)
```

---

# DP Notes Template

For Coin Change:

## State

```text
dp[x] = minimum coins required for amount x
```

---

## Transition

```text
dp[x] = min(
    dp[x],
    1 + dp[x - coin]
)
```

---

## Base Case

```text
dp[0] = 0
```

---

## Complexity

```text
Time: O(amount × coins)
Space: O(amount)
```

---

# Coin Change vs Coin Change II

| Problem        | Meaning of dp[x]       |
| -------------- | ---------------------- |
| Coin Change    | Minimum coins          |
| Coin Change II | Number of combinations |

---

# Key Learnings

## Greedy

Chooses:

```text
Best coin right now
```

May fail.

---

## DP

Checks:

```text
All valid subproblems
```

Guarantees optimal answer.

---

# Day 4 Checklist

You should be able to:

* Explain why greedy fails
* Define DP state correctly
* Write Coin Change recurrence
* Implement Memoization
* Implement Tabulation
* Explain difference between Coin Change and Coin Change II
* Recognize minimum-cost DP problems
