# Week 12 - Day 5: Longest Increasing Subsequence (LIS)

## Objective

Today you'll learn one of the most famous Dynamic Programming problems:

**Longest Increasing Subsequence (LIS)**

This problem teaches:

* Sequence DP
* Nested-loop DP
* Comparing current element with previous elements
* Building answers from earlier states

---

# Problem: Longest Increasing Subsequence (LeetCode 300)

## Problem Statement

Given an integer array:

```python
nums = [10,9,2,5,3,7,101,18]
```

Find the length of the longest strictly increasing subsequence.

Answer:

```python
4
```

One valid subsequence:

```python
[2,3,7,101]
```

---

# What is a Subsequence?

A subsequence:

* Keeps relative order
* Can skip elements

Example:

```python
nums = [10,9,2,5,3,7]
```

Valid subsequences:

```python
[10, 5]

[2, 5, 7]

[9, 7]
```

Invalid:

```python
[7, 2]
```

Order changed.

---

# DP State

## Definition

```text
dp[i] = length of LIS ending at index i
```

Meaning:

```python
dp[4]
```

stores:

```text
Longest increasing subsequence that must end at index 4
```

---

# Initial State

Every element can form a subsequence by itself.

```python
dp = [1] * n
```

Example:

```python
nums = [10,9,2]
```

Initially:

```python
dp = [1,1,1]
```

---

# Transition

For every previous element:

```python
j < i
```

Check:

```python
nums[j] < nums[i]
```

If true:

```text
Current element can extend the subsequence ending at j
```

Transition:

```text
dp[i] = max(
    dp[i],
    dp[j] + 1
)
```

---

# Visualization

Example:

```python
nums = [10,9,2,5,3,7]
```

Initial:

```python
dp = [1,1,1,1,1,1]
```

---

## i = 3

```python
nums[3] = 5
```

Check previous:

```python
10 < 5 ❌

9 < 5 ❌

2 < 5 ✅
```

Update:

```python
dp[3] = max(
    1,
    dp[2] + 1
)
```

```python
dp[3] = 2
```

---

## i = 5

```python
nums[5] = 7
```

Check:

```python
2 < 7
5 < 7
3 < 7
```

Possible lengths:

```python
dp[2] + 1 = 2

dp[3] + 1 = 3

dp[4] + 1 = 3
```

Best:

```python
dp[5] = 3
```

---

Final:

```python
dp = [1,1,1,2,2,3]
```

Answer:

```python
max(dp)
```

```python
3
```

---

# Brute Force

Try every subsequence.

```python
from typing import List

def lengthOfLIS(nums: List[int]) -> int:

    n = len(nums)

    def dfs(i, prev):

        if i == n:
            return 0

        skip = dfs(i + 1, prev)

        take = 0

        if prev == -1 or nums[i] > nums[prev]:
            take = 1 + dfs(i + 1, i)

        return max(take, skip)

    return dfs(0, -1)
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

def lengthOfLIS(nums: List[int]) -> int:

    n = len(nums)

    memo = {}

    def dfs(i, prev):

        if i == n:
            return 0

        if (i, prev) in memo:
            return memo[(i, prev)]

        skip = dfs(i + 1, prev)

        take = 0

        if prev == -1 or nums[i] > nums[prev]:
            take = 1 + dfs(i + 1, i)

        memo[(i, prev)] = max(take, skip)

        return memo[(i, prev)]

    return dfs(0, -1)
```

### Complexity

```text
Time: O(n²)

Space: O(n²)
```

---

# Tabulation (Classic DP)

```python
from typing import List

def lengthOfLIS(nums: List[int]) -> int:

    n = len(nums)

    dp = [1] * n

    for i in range(n):

        for j in range(i):

            if nums[j] < nums[i]:

                dp[i] = max(
                    dp[i],
                    dp[j] + 1
                )

    return max(dp)
```

### Complexity

```text
Time: O(n²)

Space: O(n)
```

---

# Example Walkthrough

```python
nums = [10,9,2,5,3,7,101,18]
```

Final DP:

```python
[1,1,1,2,2,3,4,4]
```

Answer:

```python
4
```

---

# DP Notes Template

## State

```text
dp[i] = length of LIS ending at index i
```

---

## Transition

```text
if nums[j] < nums[i]:

dp[i] = max(
    dp[i],
    dp[j] + 1
)
```

---

## Base Case

```text
dp[i] = 1
```

Every element is a subsequence of length 1.

---

## Complexity

```text
Time: O(n²)

Space: O(n)
```

---

# Pattern Recognition

When you see:

* Longest subsequence
* Increasing sequence
* Sequence comparison
* Compare current with previous elements

Think:

```text
Sequence DP
```

---

# Key Learnings

### Climbing Stairs

```text
dp[i] depends on dp[i-1], dp[i-2]
```

---

### House Robber

```text
Take or Skip
```

---

### Coin Change

```text
Minimum Cost DP
```

---

### LIS

```text
Compare current element with all previous elements
```

---

# Day 5 Checklist

You should be able to:

* Define LIS state
* Explain why dp starts with 1
* Write the recurrence
* Implement O(n²) DP
* Trace the DP array manually
* Identify sequence-based DP problems