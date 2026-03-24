# 📅 DAY 4 — Hashing Deep Dive (Contains Duplicate)

## 🎯 Today’s Target

By the end of today, you should:

* Understand **fast lookup using hash structures**
* Know **HashSet vs HashMap**
* Solve **duplicate-check problems** in 5–10 minutes

---

# 🧠 Step 1 — Concept: Fast Lookup & Frequency Counting

* Arrays = O(n) to check each element
* Hash structures → **O(1) lookup**
* Common types:

| Structure | Purpose                         |
| --------- | ------------------------------- |
| HashSet   | Store unique elements           |
| HashMap   | Store key → value (e.g., count) |

**Pattern:** “Check if already seen” → **HashSet**

---

# 🔥 Step 2 — Problem: Contains Duplicate

**Problem:**

Given an array, check if **any element appears more than once**.

**Example:**

```python id="3v8z5f"
nums = [1, 2, 3, 1] → True
nums = [1, 2, 3, 4] → False
```

---

# ✅ Step 3 — HashSet Solution

```python id="qj5sn8"
def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

**Logic:**

* If element already seen → duplicate found
* Else → add to set

Time Complexity = **O(n)**
Space Complexity = **O(n)**

---

# ✅ Step 4 — Optional HashMap Solution

```python id="p2qsnx"
def containsDuplicate(nums):
    freq = {}
    for num in nums:
        if num in freq:
            return True
        freq[num] = 1
    return False
```

* Works the same way
* Slightly heavier than Set if you don’t need counts

---

# 🧠 Step 5 — Dry Run (5 min)

```python id="ym3k4e"
nums = [1, 3, 2, 4, 2]
```

| Step | num | seen/set  | Duplicate?        |
| ---- | --- | --------- | ----------------- |
| 1    | 1   | {1}       | No                |
| 2    | 3   | {1,3}     | No                |
| 3    | 2   | {1,2,3}   | No                |
| 4    | 4   | {1,2,3,4} | No                |
| 5    | 2   | {1,2,3,4} | Yes → return True |

---

# 🧠 Step 6 — Pattern Recognition

Whenever you see:

* “Check duplicates”
* “Count frequencies”

Think **HashSet / HashMap**

**Pattern Variables:**

```python id="g0v7mn"
seen = set()  # or freq = {}
```

---

# 🧪 Step 7 — Your Tasks

1. Solve **Contains Duplicate** in **5–10 min**
2. Try **both HashSet and HashMap** approaches
3. Explain in words:

> “I store seen elements. If I see it again → duplicate.”

---

# ⚠️ Mistakes to Avoid

❌ Using brute-force (nested loops)
❌ Forgetting O(1) lookup
❌ Not testing multiple inputs

---

