# 🔵 DAY 4 - Boundary Search (First / Last Occurrence)

Today is where binary search becomes **powerful**.

You stop searching exact values...

and start searching **boundaries**.

This pattern is extremely common in interviews.

---

# 🎯 Goal

Master:

* First occurrence
* Last occurrence
* Lower bound
* Upper bound
* First True / Last False

---

# 🧠 Core Insight

Normal binary search asks:

> Is target at mid?

Boundary binary search asks:

> Where does a condition change?

Example:

```python id="r3d1vk"
False False False True True True
```

Need first True.

That transition point is the answer.

---

# 🔥 Real Meaning of Lower Bound

Lower bound = first index where:

```python id="8u4npe"
nums[i] >= target
```

---

# Example

```python id="4m2wbo"
nums = [1,2,4,4,4,7]
target = 4
```

Lower bound = index **2**

(first place where value becomes 4 or more)

---

# 🔥 Real Meaning of Upper Bound

Upper bound = first index where:

```python id="r5v9tj"
nums[i] > target
```

For same array:

```python id="cq1wxa"
nums = [1,2,4,4,4,7]
```

Upper bound = index **5**

(first number greater than 4)

---

# 🎯 Why Important?

Then:

### First occurrence:

```python id="u2m7go"
lower_bound(target)
```

### Last occurrence:

```python id="x0q4zr"
upper_bound(target) - 1
```

---

# 🧩 Generic Lower Bound Code

```python id="k7t5ny"
def lower_bound(nums, target):
    left, right = 0, len(nums)

    while left < right:
        mid = (left + right)//2

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left
```

---

# ⚠️ Notice Something Important

We use:

```python id="p9f4dc"
while left < right
```

Not `<=`

Because now we are shrinking a range, not checking exact target.

---

# 🧠 Problem 278 - First Bad Version

---

You have versions:

```python id="d2m6wa"
1 2 3 4 5
```

And API:

```python id="e8j3qy"
isBadVersion(x)
```

Example:

```python id="g6w1pk"
False False True True True
```

Need first bad = 3

---

# 🔥 Binary Search View

This is:

```python id="y4c8zs"
False False True True True
```

Need first True.

---

# Code

```python id="b7p1kv"
def firstBadVersion(n):
    left, right = 1, n

    while left < right:
        mid = (left + right)//2

        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1

    return left
```

---

# Why `right = mid` not `mid - 1`?

Because `mid` might itself be first bad.

Do not discard it.

Very important.

---

# 🧠 Problem 34 - First and Last Position

Input:

```python id="v6x2rn"
nums = [5,7,7,8,8,10]
target = 8
```

Output:

```python id="u3j9le"
[3,4]
```

---

# Strategy

### First position:

Lower bound of 8

### Last position:

Upper bound of 8 minus 1

---

# Code

```python id="z5h7pd"
def searchRange(nums, target):
    def lower_bound(x):
        left, right = 0, len(nums)

        while left < right:
            mid = (left + right)//2

            if nums[mid] < x:
                left = mid + 1
            else:
                right = mid

        return left

    first = lower_bound(target)
    last = lower_bound(target + 1) - 1

    if first == len(nums) or nums[first] != target:
        return [-1, -1]

    return [first, last]
```

---

# 🔍 Dry Run

```python id="t8m4vc"
nums = [5,7,7,8,8,10]
target = 8
```

Lower bound(8):

first index where value >= 8 = 3

Lower bound(9):

first index where value >= 9 = 5

So:

```python id="g9r2yw"
last = 5 - 1 = 4
```

Answer:

```python id="q7k1nf"
[3,4]
```

---

# 💀 Common Mistakes

## Mistake 1

Using normal binary search for duplicates.

Returns random 8, not first/last.

---

## Mistake 2

Using:

```python id="n1w7od"
right = mid - 1
```

when finding boundary.

May skip answer.

---

## Mistake 3

Using `<=` loop carelessly.

Boundary search usually uses:

```python id="v8f6ma"
while left < right
```

---

# 🧠 Interview Pattern Recognition

If question says:

* First occurrence
* Last occurrence
* Earliest valid index
* Minimum satisfying value
* Transition point

Think:

> Boundary Binary Search

---

# 🏆 Outcome Today

After Day 4 you should be able to:

✅ Find first occurrence
✅ Find last occurrence
✅ Solve First Bad Version
✅ Understand lower/upper bound deeply

---

# 🔥 Homework

Solve:

1. 278 First Bad Version
2. 34 Find First and Last Position

Then explain:

> Why `right = mid` is used in boundary search.

---
