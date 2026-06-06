# Day 1: Dynamic Programming Foundations

## Topics Covered

* Recursion vs Dynamic Programming
* Memoization (Top-down DP)
* Tabulation (Bottom-up DP)
* Core DP intuition building
* Problems:

  * Fibonacci Number (LeetCode 509)
  * Min Cost Climbing Stairs (LeetCode 746)

---

# Folder Structure

```
Day1
└── Problems
    ├── 509. Fibonacci Number
    │   ├── BruteForce.py
    │   ├── Memoization.py
    │   └── Tabulation.py
    └── 746. Min Cost Climbing Stairs
        ├── BruteForce.py
        ├── Memoization.py
        └── Tabulation.py
```

---

# 1. Fibonacci Number (LeetCode 509)

## Problem Definition

```
F(n) = F(n-1) + F(n-2)
```

---

## Brute Force Approach

```python
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

n = 5
print(fib(n))
```

### Complexity

* Time: O(2^n)
* Space: O(n)

---

## Memoization (Top-down DP)

```python
def fib(n: int) -> int:
    memo = {0: 0, 1: 1}

    def f(x):
        if x in memo:
            return memo[x]

        memo[x] = f(x-1) + f(x-2)
        return memo[x]

    return f(n)

n = 5
print(fib(n))
```

### Complexity

* Time: O(n)
* Space: O(n)

---

## Tabulation (Bottom-up DP)

```python
def fib(n: int) -> int:
    if n < 2:
        return n

    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

n = 5
print(fib(n))
```

### Complexity

* Time: O(n)
* Space: O(n)

---

# 2. Min Cost Climbing Stairs (LeetCode 746)

## Problem Definition

You can climb 1 or 2 steps. Each step has a cost. Find minimum cost to reach the top.

---

## Brute Force Approach

```python
from typing import List

def minCostClimbingStairs(cost: List[int]) -> int:
    n = len(cost)

    def min_cost(i):
        if i < 2:
            return 0

        return min(
            cost[i-1] + min_cost(i-1),
            cost[i-2] + min_cost(i-2),
        )

    return min_cost(n)

cost = [10, 15, 20]
print(minCostClimbingStairs(cost))
```

### Complexity

* Time: Exponential
* Space: O(n)

---

## Memoization (Top-down DP)

```python
from typing import List

def minCostClimbingStairs(cost: List[int]) -> int:
    n = len(cost)
    memo = {0: 0, 1: 0}

    def min_cost(i):
        if i in memo:
            return memo[i]

        memo[i] = min(
            cost[i-1] + min_cost(i-1),
            cost[i-2] + min_cost(i-2),
        )

        return memo[i]

    return min_cost(n)

cost = [10, 15, 20]
print(minCostClimbingStairs(cost))
```

---

## Tabulation (Bottom-up DP)

```python
from typing import List

def minCostClimbingStairs(cost: List[int]) -> int:
    n = len(cost)

    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 0

    for i in range(2, n + 1):
        dp[i] = min(
            cost[i-1] + dp[i-1],
            cost[i-2] + dp[i-2],
        )

    return dp[n]

cost = [10, 15, 20]
print(minCostClimbingStairs(cost))
```

---

# Key Learnings

## 1. DP Core Idea

Avoid repeated computation by storing results of subproblems.

---

## 2. DP Workflow

1. Write recursion
2. Identify repeated calls
3. Add memoization
4. Convert to tabulation

---

## 3. State Definition

Fibonacci:

```
dp[i] = Fibonacci value at i
```

Min Cost Climbing Stairs:

```
dp[i] = minimum cost to reach step i
```

---

## 4. DP Identification Pattern

Use DP when:

* Minimum cost
* Maximum value
* Number of ways
* Repeated overlapping computations

---

# Day 1 Completion Checklist

You should be able to:

* Explain DP in simple terms
* Write Fibonacci in recursion, memoization, tabulation
* Solve Climbing Stairs logic
* Convert recursion into DP

---