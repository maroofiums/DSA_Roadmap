# Week 12 - Day 3: House Robber Pattern

## Objective

Today focuses on one of the most important Dynamic Programming patterns:

**Take or Skip**

This pattern appears in many interview problems:

* House Robber
* House Robber II
* Delete and Earn
* Maximum Sum of Non-Adjacent Elements
* Stock Trading DP

---

# Problem: House Robber (LeetCode 198)

## Problem Statement

You are given an array `nums`.

* `nums[i]` = money in house `i`
* Adjacent houses cannot be robbed together

Return the maximum amount of money you can rob.

Example:

```python
nums = [2, 7, 9, 3, 1]
```

Answer:

```python
12
```

Rob houses:

```python
2 + 9 + 1 = 12
```

---

# DP State

## Definition

```text
dp[i] = maximum money that can be robbed from houses [0...i]
```

Meaning:

```python
dp[0]
```

stores best answer up to house 0.

```python
dp[4]
```

stores best answer up to house 4.

---

# Choices

At every house we have two options:

## Option 1: Skip Current House

Take the answer from previous house.

```text
dp[i-1]
```

---

## Option 2: Rob Current House

If we rob current house:

```text
nums[i]
```

then we cannot rob:

```text
i-1
```

So we add:

```text
nums[i] + dp[i-2]
```

---

# Transition

Take the better choice:

```text
dp[i] = max(
    dp[i-1],
    nums[i] + dp[i-2]
)
```

---

# Visual Example

```python
nums = [2, 7, 9, 3, 1]
```

### Initial

```python
dp[0] = 2
dp[1] = max(2, 7) = 7
```

### House 2

```python
max(
    7,
    9 + 2
)
```

```python
dp[2] = 11
```

---

### House 3

```python
max(
    11,
    3 + 7
)
```

```python
dp[3] = 11
```

---

### House 4

```python
max(
    11,
    1 + 11
)
```

```python
dp[4] = 12
```

---

Final DP:

```python
[2, 7, 11, 11, 12]
```

Answer:

```python
12
```

---

# Brute Force

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
```

### Complexity

```text
Time: O(2^n)
Space: O(n)
```

---

# Memoization

```python
from typing import List

def rob(nums: List[int]) -> int:
    n = len(nums)

    if n == 1:
        return nums[0]

    memo = {
        0: nums[0],
        1: max(nums[0], nums[1])
    }

    def helper(i):
        if i in memo:
            return memo[i]

        memo[i] = max(
            nums[i] + helper(i-2),
            helper(i-1)
        )

        return memo[i]

    return helper(n-1)
```

### Complexity

```text
Time: O(n)
Space: O(n)
```

---

# Tabulation

```python
from typing import List

def rob(nums: List[int]) -> int:
    n = len(nums)

    if n == 1:
        return nums[0]

    dp = [0] * n

    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(
            dp[i-1],
            nums[i] + dp[i-2]
        )

    return dp[n-1]
```

### Complexity

```text
Time: O(n)
Space: O(n)
```

---

# Space Optimized DP

Notice:

```text
dp[i]
```

only depends on:

```text
dp[i-1]
dp[i-2]
```

Therefore we only need two variables.

```python
from typing import List

def rob(nums: List[int]) -> int:
    prev2 = 0
    prev1 = 0

    for money in nums:
        current = max(
            prev1,
            money + prev2
        )

        prev2 = prev1
        prev1 = current

    return prev1
```

### Complexity

```text
Time: O(n)
Space: O(1)
```

---

# DP Template for Notes

For every DP problem, write these four things:

## 1. State

```text
What does dp[i] represent?
```

Example:

```text
dp[i] = maximum money up to house i
```

---

## 2. Transition

```text
How is dp[i] calculated?
```

Example:

```text
dp[i] = max(
    dp[i-1],
    nums[i] + dp[i-2]
)
```

---

## 3. Base Case

```text
dp[0] = nums[0]
dp[1] = max(nums[0], nums[1])
```

---

## 4. Complexity

```text
Time: O(n)
Space: O(n)
```

or

```text
Time: O(n)
Space: O(1)
```

---

# Day 3 Checklist

You should be able to:

* Explain the Take-or-Skip pattern
* Define DP state correctly
* Derive the recurrence yourself
* Implement Brute Force
* Implement Memoization
* Implement Tabulation
* Implement Space Optimization
* Identify similar problems using the same pattern
