# 📅 DAY 1 — Array Basics + Two Sum (Execution Plan)

## 🎯 Today’s Target

By the end of today, you must:

* Understand **why brute force is bad**
* Learn **HashMap thinking**
* Solve **Two Sum without memorizing code**

---

# 🧠 Step 1 — Array Thinking (15–20 min)

Before coding, fix your mindset:

👉 Array = continuous memory + index-based access
👉 Most problems = **loop + condition**

### Practice mentally:

Given:

```
[2, 7, 11, 15]
```

Think:

* How do I access each element?
* How do I compare elements?

---

# 🔥 Step 2 — Two Sum (Core Problem)

### Problem:

Find 2 numbers such that:

```
nums[i] + nums[j] = target
```

---

## ❌ Brute Force Thinking (IMPORTANT)

```python
for i in range(n):
    for j in range(i+1, n):
        if nums[i] + nums[j] == target:
            return [i, j]
```

### ❗ Understand:

* You are checking **every pair**
* Time complexity = **O(n²)**

👉 This is your **baseline thinking**

---

## ✅ Optimized Thinking (REAL LEARNING)

### Key Idea:

Instead of checking later…

👉 “Can I know the answer BEFORE I reach it?”

---

### 💡 Core Logic:

For each number:

```
complement = target - current
```

👉 Check:

* “Have I already seen this complement?”

---

## ✅ HashMap Solution

```python
def twoSum(nums, target):
    hashmap = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in hashmap:
            return [hashmap[complement], i]

        hashmap[num] = i
```

---

# 🧠 THE PATTERN (MOST IMPORTANT PART)

👉 Whenever you see:

* Pair problems
* Sum = target
* Need fast lookup

🔥 Think:

```
HashMap → store value → lookup complement
```

---

# 🧪 Step 3 — Dry Run (MANDATORY)

Example:

```
nums = [2, 7, 11, 15], target = 9
```

| Step | num | complement | hashmap | action  |
| ---- | --- | ---------- | ------- | ------- |
| 1    | 2   | 7          | {}      | store 2 |
| 2    | 7   | 2          | {2:0}   | FOUND   |

👉 Answer = [0,1]

---

# 🧪 Step 4 — Your Tasks (DO THIS SERIOUSLY)

## Task 1:

Solve Two Sum yourself (don’t copy)

---

## Task 2:

Close code and explain:

* Why brute force is slow?
* Why HashMap works?

---

## Task 3:

Re-code from memory

---

## Task 4 (MOST IMPORTANT 🔥):

Change input and test:

```
[3, 2, 4], target = 6
[3, 3], target = 6
```

---

# ⚠️ Mistakes You Must Avoid Today

❌ Memorizing code <br>
❌ Skipping dry run<br>
❌ Not understanding “why complement works”

