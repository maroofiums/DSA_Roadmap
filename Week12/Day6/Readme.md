# Week 12 - Day 6: 2D Dynamic Programming Basics

## Objective

Until now, all DP problems used a single state:

```text
dp[i]
```

Examples:

* Climbing Stairs
* House Robber
* Coin Change
* LIS

Today you'll learn 2D DP, where the state depends on:

```text
row + column
```

instead of:

```text
single index
```

---

# What is 2D DP?

In 1D DP:

```text
dp[i]
```

stores information for one position.

In 2D DP:

```text
dp[r][c]
```

stores information for a cell in a grid.

General form:

```text
dp[row][column]
```

---

# Problem 1: Unique Paths (LeetCode 62)

## Problem Statement

A robot starts at:

```text
(0,0)
```

and wants to reach:

```text
(m-1,n-1)
```

Allowed moves:

* Right
* Down

Find the number of unique paths.

---

## Example

Grid:

```text
S . .
. . .
. . E
```

Answer:

```text
6
```

---

# DP State

## Definition

```text
dp[r][c] = number of ways to reach cell (r,c)
```

---

# Key Observation

To reach:

```text
(r,c)
```

Robot can only come from:

```text
(r-1,c)
```

or

```text
(r,c-1)
```

---

# Transition

```text
dp[r][c] =
dp[r-1][c] +
dp[r][c-1]
```

---

# Base Case

Start cell:

```text
dp[0][0] = 1
```

There is exactly one way to stand at the start.

---

# Visualization

Grid:

```text
1 1 1
1 ? ?
1 ? ?
```

Fill:

```text
1 1 1
1 2 3
1 3 6
```

Answer:

```text
6
```

---

# Memoization

```python
def uniquePaths(m: int, n: int) -> int:

    memo = {}

    def dfs(r, c):

        if r == m-1 and c == n-1:
            return 1

        if r >= m or c >= n:
            return 0

        if (r, c) in memo:
            return memo[(r, c)]

        memo[(r, c)] = (
            dfs(r + 1, c) +
            dfs(r, c + 1)
        )

        return memo[(r, c)]

    return dfs(0, 0)
```

### Complexity

```text
Time: O(m × n)

Space: O(m × n)
```

---

# Tabulation

```python
def uniquePaths(m: int, n: int) -> int:

    dp = [[0] * n for _ in range(m)]

    dp[0][0] = 1

    for r in range(m):
        for c in range(n):

            if r == 0 and c == 0:
                continue

            top = dp[r-1][c] if r > 0 else 0
            left = dp[r][c-1] if c > 0 else 0

            dp[r][c] = top + left

    return dp[m-1][n-1]
```

### Complexity

```text
Time: O(m × n)

Space: O(m × n)
```

---

# Problem 2: Unique Paths II (LeetCode 63)

## Difference

Some cells contain obstacles.

```text
1 = obstacle

0 = free cell
```

---

## Example

```text
0 0 0
0 1 0
0 0 0
```

Answer:

```text
2
```

---

# DP State

```text
dp[r][c]
=
number of ways to reach cell (r,c)
```

---

# Additional Rule

Obstacle cell:

```text
dp[r][c] = 0
```

because it cannot be reached.

---

# Transition

Same as Unique Paths:

```text
dp[r][c]
=
dp[r-1][c]
+
dp[r][c-1]
```

---

# Tabulation

```python
from typing import List

def uniquePathsWithObstacles(
    obstacleGrid: List[List[int]]
) -> int:

    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    dp = [[0] * n for _ in range(m)]

    if obstacleGrid[0][0] == 1:
        return 0

    dp[0][0] = 1

    for r in range(m):
        for c in range(n):

            if obstacleGrid[r][c] == 1:
                dp[r][c] = 0
                continue

            if r == 0 and c == 0:
                continue

            top = dp[r-1][c] if r > 0 else 0
            left = dp[r][c-1] if c > 0 else 0

            dp[r][c] = top + left

    return dp[m-1][n-1]
```

### Complexity

```text
Time: O(m × n)

Space: O(m × n)
```

---

# 1D DP vs 2D DP

| 1D DP              | 2D DP               |
| ------------------ | ------------------- |
| dp[i]              | dp[r][c]            |
| One state variable | Two state variables |
| Array problems     | Grid problems       |
| Linear movement    | Row/Column movement |

---

# Grid DP Thinking Process

Whenever you see:

```text
Grid
Matrix
Board
Maze
Rows and Columns
```

Ask:

```text
Can dp[r][c] represent this cell?
```

---

# DP Notes Template

## State

```text
dp[r][c]
=
number of ways to reach cell (r,c)
```

---

## Transition

```text
dp[r][c]
=
dp[r-1][c]
+
dp[r][c-1]
```

---

## Base Case

```text
dp[0][0] = 1
```

---

## Complexity

```text
Time: O(m × n)

Space: O(m × n)
```

---

# Pattern Recognition

### Climbing Stairs

```text
dp[i]
```

Single position.

---

### House Robber

```text
dp[i]
```

Single position.

---

### Coin Change

```text
dp[amount]
```

Single position.

---

### LIS

```text
dp[i]
```

Single position.

---

### Unique Paths

```text
dp[row][col]
```

Grid position.

---

# Day 6 Checklist

You should be able to:

* Explain what 2D DP is
* Define a grid state
* Write `dp[r][c]`
* Derive the transition
* Solve Unique Paths
* Solve Unique Paths II
* Recognize grid-based DP problems
