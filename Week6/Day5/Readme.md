# 🔵 DAY 5 - Peak & Mountain Problems

Today you learn something powerful:

> Binary Search does **not** require fully sorted arrays.

It can also work when the array has a **shape**.

Examples:

* Increasing then decreasing
* Mountain array
* Local peak exists
* Slope changes direction

This is called:

> Binary Search on structure / shape

---

# 🎯 Goal

Learn to solve:

* Peak Element
* Mountain Array
* Slope-based binary search

---

# 🧠 Core Insight

Instead of checking:

> Is left side sorted?

Now we check:

> Is slope going up or down?

---

# Example

```python id="m4z8wn"
[1,2,3,1]
```

At index 1 → 2
At index 2 → 3

Slope rising.

Peak lies right side.

---

# Another Example

```python id="h7k3pa"
[1,2,3,5,4,2]
```

At 5 → next is 4

Slope falling.

Peak is left side or current.

---

# 🔥 Main Rule

If:

```python id="u8q5rc"
nums[mid] < nums[mid+1]
```

Slope rising ⬆️

Peak is right side.

```python id="v1m9xy"
left = mid + 1
```

---

If:

```python id="j6d2ot"
nums[mid] > nums[mid+1]
```

Slope falling ⬇️

Peak is left side including mid.

```python id="r4p8na"
right = mid
```

---

# ⚠️ Why `right = mid` ?

Because mid may itself be peak.

Do not discard it.

---

# 🧩 Problem 162 - Find Peak Element

Peak means:

```python id="q1n7ld"
nums[i] > nums[i-1]
nums[i] > nums[i+1]
```

Return any peak index.

---

# Example

```python id="n3x8he"
nums = [1,2,3,1]
```

Peak = index 2

---

# ✅ Code

```python id="c7m2yf"
def findPeakElement(nums):
    left, right = 0, len(nums)-1

    while left < right:
        mid = (left + right)//2

        if nums[mid] < nums[mid+1]:
            left = mid + 1
        else:
            right = mid

    return left
```

---

# 🔍 Dry Run

```python id="f2k9vt"
nums = [1,2,3,1]
```

---

### Step 1

```python id="z6m4dp"
left=0 right=3
mid=1 -> nums[1]=2
nums[2]=3
```

Since:

```python id="w9t1ra"
2 < 3
```

Go right:

```python id="d5q7ln"
left = 2
```

---

### Step 2

```python id="y3p8ko"
left=2 right=3
mid=2 -> 3
nums[3]=1
```

Since:

```python id="s1n6ew"
3 > 1
```

Go left including mid:

```python id="u2v9hf"
right = 2
```

Now:

```python id="e7c3mj"
left = right = 2
```

Peak found.

---

# 🧠 Why This Works

If slope rising:

There must be peak ahead.

If slope falling:

Peak already reached or behind.

---

# 🏔️ Problem 852 - Peak Index in Mountain Array

Mountain array means:

* strictly increasing
* then strictly decreasing

Example:

```python id="x8r4po"
[0,2,5,3,1]
```

Peak index = 2

---

# Same Exact Logic

```python id="t4n7ya"
nums[mid] < nums[mid+1] → go right
else → go left
```

---

# Code

```python id="b5m1qd"
def peakIndexInMountainArray(arr):
    left, right = 0, len(arr)-1

    while left < right:
        mid = (left + right)//2

        if arr[mid] < arr[mid+1]:
            left = mid + 1
        else:
            right = mid

    return left
```

---

# 💀 Common Mistakes

## Mistake 1

Using normal binary search.

No target exists.

We search peak position.

---

## Mistake 2

Using:

```python id="h9d2zw"
right = mid - 1
```

Wrong.

Mid may be peak.

---

## Mistake 3

Accessing:

```python id="v3k8cf"
nums[mid+1]
```

without safe loop.

Use:

```python id="p6m1sx"
while left < right
```

Then `mid+1` remains valid.

---

# 🧠 Interview Pattern Recognition

If question says:

* Peak element
* Mountain array
* Bitonic array
* Increase then decrease
* Find turning point

Think:

> Binary Search on Slope

---

# 🏆 Outcome Today

After Day 5 you should be able to:

✅ Find peak using O(log n)
✅ Solve mountain problems
✅ Understand slope logic
✅ Use binary search without sorted array

---

# 🔥 Homework

Solve:

1. 162 Find Peak Element
2. 852 Peak Index in Mountain Array

Then explain:

> Why rising slope means peak exists on right.

---
