# Week 12 - Day 7: Dynamic Programming Test Day

## Rules

* No notes
* No videos
* No solution watching
* 45 minutes per problem
* Explain your approach aloud
* Write state, transition, base case, and complexity before coding

---

# Problem 1: Climbing Stairs (LeetCode 70)

## Requirements

Implement:

1. Memoization
2. Tabulation
3. Space Optimized

---

## DP Notes

### State

```text
dp[i] = number of ways to reach stair i
```

### Transition

```text
dp[i] = dp[i-1] + dp[i-2]
```

### Base Cases

```text
dp[1] = 1
dp[2] = 2
```

### Target Complexity

```text
Time: O(n)
Space: O(1)
```

---

## Self-Test Questions

Before coding answer:

1. Why is this a DP problem?
2. What causes overlapping subproblems?
3. Why does space optimization work?

---

# Problem 2: Coin Change (LeetCode 322)

## Requirements

Implement:

* Bottom-up DP only

---

## DP Notes

### State

```text
dp[x] = minimum coins required to make amount x
```

### Transition

```text
dp[x] = min(
    dp[x],
    1 + dp[x - coin]
)
```

### Base Case

```text
dp[0] = 0
```

### Target Complexity

```text
Time: O(amount × number_of_coins)
Space: O(amount)
```

---

## Self-Test Questions

Before coding answer:

1. Why does greedy fail?
2. What does dp[x] represent?
3. Why is dp[0] equal to 0?
4. What value should represent an impossible state?

Expected answer:

```python
float("inf")
```

---

# Problem 3: Longest Increasing Subsequence (LeetCode 300)

## Requirements

Implement:

* O(n²) Dynamic Programming solution

Do not use the O(n log n) approach yet.

---

## DP Notes

### State

```text
dp[i] = length of LIS ending at index i
```

### Transition

```text
if nums[j] < nums[i]:

dp[i] = max(
    dp[i],
    dp[j] + 1
)
```

### Base Case

```text
dp[i] = 1
```

Every element alone is an increasing subsequence.

### Target Complexity

```text
Time: O(n²)
Space: O(n)
```

---

## Self-Test Questions

Before coding answer:

1. Why do we initialize dp with 1?
2. Why do we check every previous index?
3. What does "ending at i" mean?
4. Why do we return max(dp) instead of dp[n-1]?

---

# Submission Template

For each problem, write:

## State

```text
...
```

## Transition

```text
...
```

## Base Case

```text
...
```

## Complexity

```text
Time:
Space:
```

## Code

```python
# solution
```

---

# Week 12 Final Evaluation

You pass Week 12 if you can solve:

* Fibonacci
* Climbing Stairs
* Min Cost Climbing Stairs
* House Robber
* Coin Change
* Coin Change II
* Longest Increasing Subsequence
* Unique Paths
* Unique Paths II

and explain for each:

```text
State
Transition
Base Case
Complexity
```

---
