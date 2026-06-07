# Week 12 - Day 2: Climbing Stairs + House Robber (DP Patterns)

## Topics Covered

* Recursion to DP conversion
* Memoization (Top-down DP)
* Tabulation (Bottom-up DP)
* 1D DP patterns
* “Take or Skip” pattern (House Robber)
* “Fibonacci-style DP” (Climbing Stairs)

---

# Folder Structure

```text
Day2
└── Problems
    ├── 198. House Robber
    │   ├── BruteForce.py
    │   ├── Memoization.py
    │   └── Tabulation.py
    └── 70. Climbing Stairs
        ├── BruteForce.py
        ├── Memoization.py
        └── Tabulation.py
```

---

# 1. Climbing Stairs (LeetCode 70)

## Problem Idea

You can climb:

* 1 step
* 2 steps

Find number of ways to reach step n.

---

## Recurrence Relation

```text
f(n) = f(n-1) + f(n-2)
```

---

# Brute Force (Recursion)

```python
def climbStairs(n: int) -> int:
    if n <= 2:
        return n

    return climbStairs(n-1) + climbStairs(n-2)

n = 3
print(climbStairs(n))
```

### Complexity

* Time: O(2^n)
* Space: O(n)

---

# Memoization (Top-down DP)

```python
def climbStairs(n: int) -> int:

    memo = {1: 1, 2: 2}

    def dfs(x):
        if x in memo:
            return memo[x]

        memo[x] = dfs(x-1) + dfs(x-2)
        return memo[x]

    return dfs(n)

n = 3
print(climbStairs(n))
```

### Complexity

* Time: O(n)
* Space: O(n)

---

# Tabulation (Bottom-up DP)

```python
def climbStairs(n: int) -> int:

    if n <= 2:
        return n

    dp = [0] * n
    dp[0], dp[1] = 1, 2

    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n-1]

n = 3
print(climbStairs(n))
```

### Complexity

* Time: O(n)
* Space: O(n)

---

## Key Insight

This is a Fibonacci pattern:

```text
dp[i] = dp[i-1] + dp[i-2]
```

---

# 2. House Robber (LeetCode 198)

## Problem Idea

You cannot rob two adjacent houses.

Goal:
Maximize sum of non-adjacent elements.

---

## Pattern Type

This is a:

* Take / Skip DP problem

At each index:

* Take current house
* Skip current house

---

## Recurrence

```text
dp[i] = max(nums[i] + dp[i-2], dp[i-1])
```

---

# Brute Force (Recursion)

```python
from typing import List

def rob(nums: List[int]) -> int:
    n = len(nums)

    def helper(i):
        if i == 0:
            return nums[0]

        if i == 1:
            return max(nums[0], nums[1])

        return max(
            nums[i] + helper(i-2),
            helper(i-1)
        )

    return helper(n-1)

nums = [2,7,9,3,1]
print(rob(nums))
```

### Complexity

* Time: O(2^n)
* Space: O(n)

---

# Memoization (Top-down DP)

```python
from typing import List

def rob(nums: List[int]) -> int:
    n = len(nums)

    if n == 1:
        return nums[0]

    if n == 2:
        return max(nums[0], nums[1])

    memo = {0: nums[0], 1: max(nums[0], nums[1])}

    def helper(i):
        if i in memo:
            return memo[i]

        memo[i] = max(
            nums[i] + helper(i-2),
            helper(i-1)
        )

        return memo[i]

    return helper(n-1)

nums = [2,7,9,3,1]
print(rob(nums))
```

### Complexity

* Time: O(n)
* Space: O(n)

---

# Tabulation (Bottom-up DP)

```python
from typing import List

def rob(nums: List[int]) -> int:
    n = len(nums)

    if n == 1:
        return nums[0]

    if n == 2:
        return max(nums[0], nums[1])

    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(
            nums[i] + dp[i-2],
            dp[i-1]
        )

    return dp[n-1]

nums = [2,7,9,3,1]
print(rob(nums))
```

### Complexity

* Time: O(n)
* Space: O(n)

---

# Key Learnings (Day 2)

## 1. Two Major DP Patterns

### Climbing Stairs

* Fibonacci pattern
* dp[i] = dp[i-1] + dp[i-2]

---

### House Robber

* Take / Skip pattern
* dp[i] = max(take, skip)

---

## 2. How to Identify DP Type

| Problem Type         | Pattern      |
| -------------------- | ------------ |
| Count ways           | Fibonacci DP |
| Max/Min optimization | Take/Skip DP |

---

## 3. Core Thinking Model

At every index:

* Option 1: include current element
* Option 2: exclude current element

---

## 4. DP Conversion Flow

1. Write recursion
2. Identify repeated states
3. Add memoization
4. Convert to tabulation

---

# Day 2 Completion Checklist

You should now be able to:

* Solve Climbing Stairs without help
* Recognize Fibonacci pattern instantly
* Understand House Robber logic
* Write Take/Skip DP recurrence
* Convert recursion → DP

---