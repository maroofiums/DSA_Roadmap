# DAY 5 - Greedy Algorithms Introduction

## Folder Structure

```text
Day5
├── Problems
│   ├── 455. Assign Cookies
│   │   ├── BruteForce.py
│   │   └── Optimal.py
│   ├── 860. Lemonade Change
│   │   ├── BruteForce.py
│   │   └── Optimal.py
│   └── 122. Best Time to Buy and Sell Stock II
│       ├── BruteForce.py
│       └── Optimal.py
└── Readme.md
```

---

# 1. What is a Greedy Algorithm?

A Greedy Algorithm makes the best possible choice at the current moment without worrying about future consequences.

Greedy thinking:

> "What is the best choice RIGHT NOW?"

The algorithm hopes that a sequence of locally optimal choices leads to a globally optimal solution.

---

# 2. Local Optimum vs Global Optimum

## Local Optimum

The best choice at the current step.

Example:

```text
You see $10 now.
You take it immediately.
```

Good current choice.

---

## Global Optimum

The best overall solution after considering all possibilities.

Example:

```text
Skip $10 now.
Get $100 later.
```

Better final outcome.

---

## Important

Greedy works only when:

```text
Local Optimum
        ↓
Leads to
        ↓
Global Optimum
```

---

# 3. When Does Greedy Work?

Greedy usually works when the problem has:

## Greedy Choice Property

A locally optimal choice can lead to a globally optimal solution.

---

## Optimal Substructure

After making a choice, the remaining problem can be solved optimally.

---

# 4. Greedy vs Dynamic Programming

| Greedy                   | Dynamic Programming               |
| ------------------------ | --------------------------------- |
| Makes immediate decision | Explores many possibilities       |
| Faster                   | Usually slower                    |
| Less memory              | More memory                       |
| Simpler implementation   | More complex                      |
| Doesn't always work      | Usually guarantees optimal answer |

---

## Example

### Coin Change

Coins:

```text
[1, 3, 4]
```

Target:

```text
6
```

Greedy:

```text
4 + 1 + 1 = 3 coins
```

Optimal:

```text
3 + 3 = 2 coins
```

Greedy fails.

DP succeeds.

---

# 5. How to Recognize Greedy Problems

Common clues:

* Largest first
* Smallest first
* Earliest finish time
* Maximum profit now
* Sort then decide
* Take the best available option

---

# Problem 1

## Assign Cookies

### LeetCode 455

---

### Problem

Each child has a greed factor.

Each cookie has a size.

Assign cookies to maximize satisfied children.

---

### Example

```python
g = [1,2,3]
s = [1,1]
```

Output:

```python
1
```

Only one child can be satisfied.

---

## Greedy Idea

Sort both arrays.

Always give the smallest possible cookie that satisfies the current child.

---

### Optimal Solution

```python
from typing import List

def findContentChildren(g: List[int], s: List[int]) -> int:

    g.sort()
    s.sort()

    child = 0
    cookie = 0

    while child < len(g) and cookie < len(s):

        if s[cookie] >= g[child]:
            child += 1

        cookie += 1

    return child
```

---

### Complexity

```text
O(n log n)
```

Due to sorting.

---

# Problem 2

## Lemonade Change

### LeetCode 860

---

### Problem

Each lemonade costs:

```text
$5
```

Customers pay with:

```text
5, 10, 20
```

Return correct change.

---

### Example

```python
[5,5,5,10,20]
```

Output:

```python
True
```

---

## Greedy Idea

Always prefer:

```text
$10 + $5
```

instead of

```text
$5 + $5 + $5
```

because $5 bills are more valuable for future transactions.

---

### Optimal Solution

```python
from typing import List

def lemonadeChange(bills: List[int]) -> bool:

    five = 0
    ten = 0

    for bill in bills:

        if bill == 5:
            five += 1

        elif bill == 10:

            if five == 0:
                return False

            five -= 1
            ten += 1

        else:

            if ten > 0 and five > 0:
                ten -= 1
                five -= 1

            elif five >= 3:
                five -= 3

            else:
                return False

    return True
```

---

### Complexity

```text
O(n)
```

---

# Problem 3

## Best Time to Buy and Sell Stock II

### LeetCode 122

---

### Problem

You may perform unlimited transactions.

Find maximum profit.

---

### Example

```python
prices = [7,1,5,3,6,4]
```

Output:

```python
7
```

---

### Explanation

```text
Buy at 1
Sell at 5

Profit = 4

Buy at 3
Sell at 6

Profit = 3

Total = 7
```

---

## Greedy Idea

Take every profitable increase.

Whenever:

```python
prices[i] > prices[i - 1]
```

Add the difference.

---

### Optimal Solution

```python
from typing import List

def maxProfit(prices: List[int]) -> int:

    profit = 0

    for i in range(1, len(prices)):

        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]

    return profit
```

---

### Complexity

```text
O(n)
```

---

# 6. Exchange Argument (Important Theory)

Interviewers sometimes ask:

> Why does your greedy choice work?

The exchange argument helps prove correctness.

Idea:

```text
Suppose an optimal solution does NOT make our greedy choice.

Swap its choice with our greedy choice.

Solution quality does not become worse.

Therefore greedy choice is safe.
```

---

## Example

Assign Cookies

Giving a large cookie to a less greedy child is wasteful.

Giving the smallest valid cookie is always safe.

Therefore the greedy strategy works.

---

# 7. Why Proofs Matter

Many greedy solutions look correct but fail.

Example:

```text
Coin Change
```

Greedy works for:

```text
[1,5,10,25]
```

but fails for:

```text
[1,3,4]
```

Always ask:

```text
Can I prove this greedy choice is safe?
```

---

# 8. Pattern Recognition

Common Greedy Patterns:

### Sorting + Greedy

```text
Assign Cookies
Meeting Rooms
Intervals
```

---

### Profit Maximization

```text
Stock Problems
Job Scheduling
```

---

### Resource Allocation

```text
Cookies
Gas Stations
Tasks
```

---

# 9. Interview Checklist

Before saying a problem is greedy, ask:

* What is the local optimal choice?
* Can I prove it is safe?
* Does it lead to the global optimum?
* Would DP explore more possibilities?

---

# 10. What You Learned Today

You should now understand:

* What greedy algorithms are
* Local vs global optimum
* Greedy vs DP
* Exchange argument intuition
* Why greedy proofs matter
* Three classic greedy problems

---
