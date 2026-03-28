# 📅 DAY 7 - WEEK 1 MOCK PRACTICE (README)

## 🎯 Objective

Test understanding of **Week 1 patterns** by solving problems without help and without looking at solutions.

Goal is not new learning - but **pattern recall + implementation speed**.

---

# 🧠 Problems Solved

## 1. Contains Duplicate

### 🧩 Pattern

HashSet → “Have I seen this before?”

### 💡 Idea

* Store elements in a set
* If element already exists → duplicate found

### ⏱ Complexity

* Time: O(n)
* Space: O(n)

### ✅ Key Insight

Fast lookup replaces nested loops.

---

## 2. Maximum Subarray (Kadane’s Algorithm)

### 🧩 Pattern

Kadane → “Running sum optimization”

### 💡 Idea

* Keep track of:

  * current subarray sum
  * global maximum
* If current sum becomes worse than starting fresh → reset

### ⏱ Complexity

* Time: O(n)
* Space: O(1)

### ✅ Key Insight

Negative prefix kills future subarray value → reset.

---

# 🧠 WEEK 1 CORE PATTERNS

| Problem            | Pattern      | Core Idea          |
| ------------------ | ------------ | ------------------ |
| Two Sum            | HashMap      | store complement   |
| Stock Buy/Sell     | Min Tracking | track lowest price |
| Max Subarray       | Kadane       | reset if sum < 0   |
| Contains Duplicate | HashSet      | detect repeats     |

---

# 🧠 WHAT I LEARNED

* I can recognize basic DSA patterns
* I can implement solutions without looking
* I understand when to use:

  * HashMap (pairs)
  * HashSet (duplicates)
  * Greedy min tracking (stock)
  * Kadane (subarrays)

---

# ⚠️ MISTAKES TO AVOID

* Don’t jump into code without pattern identification
* Don’t memorize solutions
* Don’t use brute force unless necessary
* Always think: “What pattern is this?”

---

# 🚀 WEEK 1 CONCLUSION

Week 1 is about:

> Moving from “random coding” → “pattern thinking”

If this foundation is strong, advanced topics (DP, graphs, sliding window) become much easier.

