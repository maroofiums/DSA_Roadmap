# 🔵 DAY 6 - Binary Search on Answer (IMPORTANT)

Today is one of the highest-value binary search patterns for interviews.

This is where many medium/hard problems become easy.

You stop searching an array...

and start searching the **answer itself**.

---

# 🎯 Goal

Use binary search for optimization problems like:

* Minimum speed
* Maximum feasible value
* Smallest capacity
* Earliest valid time
* Lowest cost satisfying condition

---

# 🧠 Core Insight

Instead of:

```python id="y1m6qp"
searching inside nums[]
```

You search inside:

```python id="q8r3na"
possible answers range
```

Example:

Koko speed can be:

```python id="r4p7vk"
1 bananas/hour to max(piles)
```

We binary search that range.

---

# 🔥 Why This Works

Because many optimization problems have:

> A monotonic condition

Meaning:

```python id="m2x8jf"
False False False True True True
```

or

```python id="c6n1ds"
True True True False False
```

Once valid, always valid after some point.

That allows binary search.

---

# Example

If speed = 2 too slow ❌
speed = 3 too slow ❌
speed = 4 works ✅
speed = 5 works ✅
speed = 6 works ✅

Need **minimum working speed** = 4

---

# 🎯 Pattern Formula

1. Define answer range
2. Write `can(mid)` function
3. If works → try smaller
4. Else → need larger

---

# 🧩 Problem 875 - Koko Eating Bananas

---

## Problem Summary

Koko has piles:

```python id="v7n4kw"
[3,6,7,11]
```

Hours:

```python id="d9m2po"
h = 8
```

Need minimum bananas/hour to finish in time.

---

# Search Space

Minimum speed:

```python id="x4r8ty"
1
```

Maximum speed:

```python id="u3p1ha"
max(piles)
```

---

# Feasibility Function

If speed = `k`

Hours needed:

```python id="f2z6me"
ceil(pile / k)
```

Total all piles.

If total ≤ h → valid.

---

# ✅ Code

```python id="t8n5qx"
import math

def minEatingSpeed(piles, h):
    left, right = 1, max(piles)

    while left < right:
        mid = (left + right)//2

        hours = sum(math.ceil(p / mid) for p in piles)

        if hours <= h:
            right = mid
        else:
            left = mid + 1

    return left
```

---

# 🔍 Dry Run

```python id="j6q2wc"
piles = [3,6,7,11], h=8
```

Try speed 6:

Hours:

```python id="g5r8na"
1 + 1 + 2 + 2 = 6
```

Valid ✅

Try smaller.

Eventually answer = 4

---

# 🧩 Problem 1011 - Capacity To Ship Packages Within D Days

---

## Summary

Weights:

```python id="p3v7kd"
[1,2,3,4,5,6,7,8,9,10]
```

Need minimum ship capacity to deliver in `D` days.

---

# Search Space

Minimum capacity:

```python id="n4m1yo"
max(weights)
```

Must fit heaviest package.

Maximum capacity:

```python id="u8t6qe"
sum(weights)
```

Carry all in one day.

---

# Feasibility Function

Given capacity `cap`

Simulate shipping:

* Add weights until overflow
* Then next day

If days used ≤ D → valid

---

# ✅ Code

```python id="b7k2pa"
def shipWithinDays(weights, D):
    left, right = max(weights), sum(weights)

    while left < right:
        mid = (left + right)//2

        days = 1
        current = 0

        for w in weights:
            if current + w > mid:
                days += 1
                current = 0
            current += w

        if days <= D:
            right = mid
        else:
            left = mid + 1

    return left
```

---

# 🧠 Universal Template

```python id="k5x9fr"
left = minimum_possible
right = maximum_possible

while left < right:
    mid = (left + right)//2

    if can(mid):
        right = mid
    else:
        left = mid + 1

return left
```

---

# ⚠️ Why `right = mid`?

Because `mid` works.

Maybe smaller valid answer exists.

---

# ⚠️ Why `left = mid + 1`?

Because `mid` fails.

Must go bigger.

---

# 💀 Common Mistakes

## Mistake 1

Wrong search range.

Need logical min/max answer.

---

## Mistake 2

Poor `can(mid)` function.

That is the heart of problem.

---

## Mistake 3

Using exact target binary search mindset.

Here we seek minimum valid value.

---

# 🧠 Interview Recognition Pattern

If problem says:

* Minimum possible
* Maximum possible
* At least / at most
* Capacity
* Speed
* Time
* Cost
* Feasible?

Think:

> Binary Search on Answer

---

# 🏆 Outcome Today

After Day 6 you should be able to:

✅ Convert optimization into binary search
✅ Write `can(mid)` checks
✅ Solve Koko Bananas
✅ Solve shipping capacity problems

---

# 🔥 Homework

Solve:

1. 875 Koko Eating Bananas
2. 1011 Capacity To Ship Packages

Then explain:

> Why valid answers form a monotonic range.

---
