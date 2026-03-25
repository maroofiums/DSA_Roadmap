# 📅 DAY 5 - Mixed Practice

## 🎯 Today’s Target

By the end of today, you should:

* Solve **Two Sum, Maximum Subarray, Contains Duplicate** without looking at solutions
* Recognize **which pattern to use immediately**
* Build confidence in **dry-running & reasoning before coding**

---

# 🔥 Step 1 - Two Sum

**Pattern:** HashMap → find complement

**Quick Mental Check:**

* Input: `[2, 7, 11, 15], target=9`
* Think: For each number, check if `target - num` is in HashMap
* Dry run → `[0,1]`

✅ Solve it **without copying code**

---

# 🔥 Step 2 - Maximum Subarray (Kadane)

**Pattern:** Running sum + reset if negative

* Input: `[-2,1,-3,4,-1,2,1,-5,4]`
* Dry run:

| Step | current_sum | max_sum | Reset?  |
| ---- | ----------- | ------- | ------- |
| -2   | -2          | -2      | Yes → 0 |
| 1    | 1           | 1       | No      |
| -3   | -2          | 1       | Yes → 0 |
| …    | …           | …       | …       |

✅ Solve without looking

---

# 🔥 Step 3 - Contains Duplicate

**Pattern:** HashSet → O(1) lookup

* Input: `[1,3,2,4,2]`
* Dry run → Duplicate found at `2`
* Solve quickly

---

# 🧠 Step 4 - Pattern Recap

| Problem            | Pattern | Key Variable(s)        |
| ------------------ | ------- | ---------------------- |
| Two Sum            | HashMap | `hashmap`              |
| Maximum Subarray   | Kadane  | `current_sum, max_sum` |
| Contains Duplicate | HashSet | `seen`                 |

---

# 🧪 Step 5 - Your Tasks

1. **Solve all 3 problems today** **without looking**
2. Dry run each manually first
3. **Explain logic in words** after solving
4. Time yourself (optional): 10–15 min per problem

---

# ⚠️ Mistakes to Avoid

❌ Jumping to code without thinking
❌ Forgetting patterns
❌ Skipping dry run

---
