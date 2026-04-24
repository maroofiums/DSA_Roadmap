# 🔵 DAY 1 - Foundations of Binary Search

## 🎯 Core Idea

Binary search is not about “finding fast”.

It is about:

> **Eliminating half the search space every step**

You never scan elements one by one.

You repeatedly ask:

> “Is my answer in the left half or right half?”

---

# 🧠 1. The Key Mental Model

You always maintain 3 pointers:

* `left` → start of search space
* `right` → end of search space
* `mid` → middle element

At every step:

You do ONE decision:

* Go left
* OR go right

Then you throw away the other half forever.

---

# 📉 2. Why O(log n)?

Because every step divides search space by 2:

T(n)=\log_2(n)

Example:

If n = 16:

```
16 → 8 → 4 → 2 → 1
```

Only 4 steps needed.

---

# ⚙️ 3. Binary Search Logic Flow

For sorted array:

```
left  = 0
right = n - 1
```

Loop:

1. Find mid
2. Compare target with mid
3. Decide direction
4. Shrink search space

---

# 💡 4. Core Code (Must Memorize)

```python
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

---

# ⚠️ 5. VERY IMPORTANT RULES

## Rule 1 - Why `left <= right`?

Because you still want to check last element.

If you use `<` → you may miss answer.

---

## Rule 2 - Why `+1` and `-1`?

Because:

If you don’t eliminate mid → infinite loop happens.

---

## Rule 3 - Sorted array is required

Binary search ONLY works when:

> Data is sorted or logically monotonic

---

# 🔍 6. Dry Run (Step-by-Step)

## Problem:

```
nums = [1, 3, 5, 7, 9]
target = 7
```

---

### Step 1:

```
left = 0
right = 4
mid = 2 → nums[2] = 5
```

5 < 7 → go right

```
left = mid + 1 = 3
```

---

### Step 2:

```
left = 3
right = 4
mid = 3 → nums[3] = 7
```

Found ✅ return 3

---

# 🧠 7. Search Insert Position (Important Pattern)

This teaches you:

> “Where should this number go?”

Example:

```
nums = [1,3,5,6], target = 2
```

Answer → index 1

---

## Code idea:

```python
if nums[mid] < target:
    left = mid + 1
else:
    right = mid - 1
```

At end → `left` is insertion point

---

# 🧩 8. What You MUST Learn Today

If you finish Day 1 properly, you should be able to:

### ✅ Write binary search without help

### ✅ Explain why it is O(log n)

### ✅ Do a dry run manually

### ✅ Understand left/right movement

### ✅ Solve:

* 704 Binary Search
* 35 Search Insert Position

---

# ⚠️ Common Beginner Mistakes

❌ Using `while left < right` blindly
❌ Forgetting `-1 / +1` updates
❌ Mid not recalculated
❌ Not understanding sorted requirement
❌ Memorizing code without logic

---

# 🚀 Final Insight (Very Important)

Binary search is NOT:

> “searching fast”

It is:

> “eliminating impossibility”

---
