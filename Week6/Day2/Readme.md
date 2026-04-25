# 🔵 DAY 2 - Implementation Mastery & Edge Cases

Today is where most beginners fail.

Many people know binary search theory… but cannot code it bug-free.

Today your goal is:

> Learn to debug binary search confidently.

---

# 🎯 Why Binary Search Breaks So Often

Because tiny mistakes cause:

* Infinite loops
* Missing target
* Wrong index
* Crashes
* Off-by-one bugs

Even experienced developers make these mistakes.

---

# 🧠 1. Off-by-One Errors

This means searching one step too far or one step too short.

Example:

```python id="mqbjl8"
while left < right:
```

vs

```python id="w9d3p7"
while left <= right:
```

These are **not the same**.

---

## Use `<=` when:

You are searching exact target and want to check final single element.

```python id="ql8m3u"
while left <= right:
```

Used in classic binary search.

---

## Use `<` when:

You are shrinking range for boundaries (advanced later).

---

# ⚠️ Example Bug

```python id="j7lf3a"
nums = [5]
target = 5
left = 0
right = 0
```

If:

```python id="v6c8jw"
while left < right:
```

Loop never runs.

Answer missed.

---

# 🧠 2. Infinite Loop Issues

Most dangerous bug.

---

## Wrong Code:

```python id="fl3qos"
left = mid
```

Why wrong?

If:

```python id="r0kqz8"
left = 4
right = 5
mid = 4
```

Then:

```python id="8v4z8p"
left = mid = 4
```

No movement.

Loop repeats forever.

---

## Correct:

```python id="o9g9ms"
left = mid + 1
```

OR

```python id="z1n9ep"
right = mid - 1
```

Always eliminate mid if already checked.

---

# 🧠 3. Correct Pointer Movement

---

## If target > nums[mid]

Answer must be right side.

```python id="u8f1tb"
left = mid + 1
```

---

## If target < nums[mid]

Answer must be left side.

```python id="0ifg7j"
right = mid - 1
```

---

## If equal:

Return answer.

---

# ⚠️ Never Do This

```python id="p2r1yk"
left = mid
right = mid
```

This often causes loops.

---

# 🧠 4. Mid Calculation Safety

Normal:

```python id="ksv9kn"
mid = (left + right) // 2
```

Works in Python.

---

## Safer universal formula:

```python id="j9r7yo"
mid = left + (right - left) // 2
```

Used in Java / C++ because large numbers can overflow.

---

# 🔍 Dry Run Example

```python id="8k3t6a"
nums = [1,3,5,7,9]
target = 9
```

---

### Step 1

```python id="5d7q3h"
left=0 right=4
mid=2 -> 5
```

Need right side:

```python id="1y6h4p"
left = 3
```

---

### Step 2

```python id="7u9m2v"
left=3 right=4
mid=3 -> 7
```

Need right:

```python id="x0k2jw"
left = 4
```

---

### Step 3

```python id="9f6l1n"
left=4 right=4
mid=4 -> 9
```

Found.

---

# 🧪 Practice Problem 1 - Sqrt(x)

Find integer square root.

Example:

```python id="9nb8vn"
x = 8
```

Real sqrt = 2.828

Return:

```python id="8h2g3f"
2
```

---

## Binary Search Idea

Search answer from:

```python id="0f6t2m"
1 to x
```

Check:

```python id="z3d1hk"
mid * mid
```

If too large → go left
Else → save answer, go right

---

## Why Important?

First intro to:

> Binary Search on values, not array

---

# 🧪 Practice Problem 2 - Guess Number Higher or Lower

API tells:

* too high
* too low
* correct

Perfect binary search problem.

Search range:

```python id="yk3f0u"
1 to n
```

---

# 🧠 Debug Checklist (Memorize)

Whenever binary search fails ask:

### 1. Loop condition correct?

```python id="3w8f1m"
<= or <
```

### 2. Mid updates each loop?

### 3. Pointers moving?

```python id="r2k6do"
+1 / -1
```

### 4. Search space shrinking?

### 5. Final return correct?

---

# 💀 Most Common Interview Bugs

## Bug 1

```python id="f7p1zt"
mid = left + right // 2
```

Wrong precedence.

Use parentheses.

---

## Bug 2

```python id="2j5rko"
right = mid
```

Can cause infinite loop.

---

## Bug 3

Using `<` instead of `<=`

Misses last candidate.

---

# 🏆 Outcome Today

After Day 2 you should be able to:

✅ Fix infinite loops<br>
✅ Handle single element arrays<br>
✅ Understand pointer movement<br>
✅ Solve sqrt(x)<br>
✅ Debug most binary search mistakes<br>

---

# 🔥 Homework

Solve:

1. 69 Sqrt(x)
2. 374 Guess Number Higher or Lower

Then write binary search from memory 3 times.

---
