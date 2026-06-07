# WEEK 12 - Dynamic Programming (DP)

This is one of the most important weeks in your entire DSA roadmap.

DP appears in:

* FAANG interviews
* Competitive programming
* AI optimization
* Reinforcement learning foundations
* Scheduling systems
* Resource allocation problems

Your goal this week is **not memorizing solutions**.

Your goal is learning:

1. How to identify DP problems
2. How to define states
3. How to write recurrence relations
4. How to optimize brute force → memoization → tabulation

---

# WEEK 12 GOALS

By the end of this week you should be able to:

* Recognize DP patterns
* Convert recursion into DP
* Use memoization
* Build tabulation solutions
* Solve classic 1D DP problems
* Understand basic 2D DP

---

# DAY 1 - DP Foundations

## Theory

Learn:

### What is Dynamic Programming?

DP = Store answers of overlapping subproblems.

Characteristics:

1. Optimal Substructure
2. Overlapping Subproblems

---

### DP Workflow

Step 1

Write recursive solution

Step 2

Identify repeated computations

Step 3

Add memoization

Step 4

Convert to tabulation

---

### Example

Climbing Stairs

```
f(n) = f(n-1) + f(n-2)
```
```math
f(n)=f(n-1)+f(n-2)
```
---

## Study

Watch/read:

* Recursion review
* Memoization
* Tabulation

---

## Practice

Easy:

1. Fibonacci Number
2. Min Cost Climbing Stairs

---

## Notes

Write:

* Memoization vs Tabulation
* Time complexity improvement

---

# DAY 2 - Climbing Stairs Pattern

This is the foundation of 1D DP.

---

## Learn

State definition

```
dp[i] = ways to reach stair i
```

Recurrence

```
dp[i] = dp[i-1] + dp[i-2]
```
```math
dp[i]=dp[i-1]+dp[i-2]
```
---

## Practice

1. Climbing Stairs
2. House Robber

---

## Focus Questions

* Why does recursion explode?
* How does memoization help?
* What does dp[i] represent?

---

# DAY 3 - House Robber Pattern

This teaches "take or skip".

---

## Learn

State:

```
dp[i] = max money until house i
```

Choice:

```
Take current
Skip current
```

Recurrence:

```
dp[i] = max(
    dp[i-1],
    nums[i] + dp[i-2]
)
```

---

## Practice

1. House Robber

---

## Write Notes

For every DP problem:

```
State
Transition
Base Case
Complexity
```

---

# DAY 4 - Coin Change

Important interview problem.

---

## Learn

State:

```
dp[x] = minimum coins for amount x
```

Transition:

```
dp[x] =
min(
dp[x],
1 + dp[x-coin]
)
```

---

## Practice

1. Coin Change
2. Coin Change II

---

## Focus

Understand:

* Why greedy fails
* Why DP succeeds

---

# DAY 5 - Longest Increasing Subsequence (LIS)

Very famous DP problem.

---

## Learn

State:

```
dp[i]
=
LIS ending at i
```

Transition:

```
if nums[j] < nums[i]

dp[i]
=
max(
dp[i],
dp[j] + 1
)
```

---

## Practice

1. Longest Increasing Subsequence

---

## Goal

Understand O(n²) solution first.

Do NOT jump to O(n log n) yet.

---

# DAY 6 - 2D DP Basics

Introduction only.

---

## Learn

When state depends on:

```
row + column
```

instead of

```
single index
```

---

## Practice

1. Unique Paths
2. Unique Paths II

State:

```
dp[r][c]
```

Meaning:

```
Ways to reach cell (r,c)
```

---

## Learn

Grid DP intuition.

---

# DAY 7 - TEST DAY

Rules:

* No notes
* No videos
* No solution watching
* 45 minutes per problem
* Explain approach aloud
* Write complexity yourself

---

## Problem 1 - Climbing Stairs

Expected:

* Memoization
* Tabulation
* Space optimized

Target:

```
Time O(n)
Space O(1)
```

---

## Problem 2 - Coin Change

Expected:

* Bottom-up DP

Target:

```
Time O(amount × coins)
```

---

## Problem 3 - Longest Increasing Subsequence

Expected:

* O(n²) DP

Target:

```
Time O(n²)
Space O(n)
```

---

# End of Week Check

You pass Week 12 if you can answer:

### DP Fundamentals

* What is overlapping subproblems?
* What is optimal substructure?
* Memoization vs tabulation?

### Climbing Stairs

* State?
* Transition?
* Complexity?

### Coin Change

* Why greedy fails?
* What does dp[i] mean?

### LIS

* What does dp[i] represent?
* Why do we check all previous elements?

### 2D DP

* When do we need dp[r][c]?
* Difference between 1D DP and 2D DP?

---
