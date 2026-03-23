# 📅 DAY 3 — Prefix Sum Basics (Maximum Subarray)

## 🎯 Today’s Target

By the end of today, you should:

* Understand **running sum** / **prefix sum**
* Master **Kadane’s Algorithm** for max subarray
* Know **why we reset sum**

---

# 🧠 Step 1 — Concept: Running Sum

Given an array:

```python
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
```

* Running sum = sum of consecutive elements
* Brute force: check **all subarrays** → O(n²) or O(n³)
* Optimized: compute **max running sum** in one pass → O(n)

---

# 🔥 Step 2 — Kadane’s Algorithm (The Core Idea)

**Observation:**

* If the running sum becomes **negative**, continuing it will **only decrease future sums**
* So reset to 0

**Algorithm:**

```python
max_sum = float('-inf')
current_sum = 0

for num in nums:
    current_sum += num
    if current_sum > max_sum:
        max_sum = current_sum
    if current_sum < 0:
        current_sum = 0
```

---

# 🧠 Step 3 — Dry Run (Most Important)

```python
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
```

| Step | num | current_sum | max_sum | Reset?  |
| ---- | --- | ----------- | ------- | ------- |
| 0    | -2  | -2          | -2      | Yes → 0 |
| 1    | 1   | 1           | 1       | No      |
| 2    | -3  | -2          | 1       | Yes → 0 |
| 3    | 4   | 4           | 4       | No      |
| 4    | -1  | 3           | 4       | No      |
| 5    | 2   | 5           | 5       | No      |
| 6    | 1   | 6           | 6       | No      |
| 7    | -5  | 1           | 6       | No      |
| 8    | 4   | 5           | 6       | No      |

✅ Answer = 6

**Key Insight:**

> Reset happens when current sum < 0 → negative sum cannot help future subarrays

---

# 🧠 Step 4 — Pattern Recognition

Whenever you see:

* “Max/Min sum of subarray”
* “Continuous elements”

Think **Kadane → running sum + reset if negative**

**Pattern Variables:**

```python
current_sum, max_sum
```

---

# 🧪 Step 5 — Your Tasks

1. **Dry run manually** on:

```python
nums = [1, -2, 3, 10, -4, 7, 2, -5] → Answer?
nums = [-1, -2, -3, -4] → Answer?
```

2. Explain in words **why reset happens**:

> Negative sum reduces future subarray sum → discard it

3. Write pattern in your notebook:

> “Subarray optimization → Kadane”

---

# ⚠️ Mistakes to Avoid

❌ Thinking in brute-force
❌ Forgetting to reset
❌ Trying to memorize code instead of pattern

---
