# **Week 1 — Day 1: Array Basics**

## **Goal**

* Understand **array traversal, max/min finding, prefix sums**
* Start recognizing **patterns in array problems**
* Solve **basic problems confidently**

---

## **Concepts to Cover**

1. **Array Traversal**

   * Loop through all elements
   * Access by index
   * Examples:

     ```python
     nums = [3, 1, 4, 2]
     for i in range(len(nums)):
         print(nums[i])
     for num in nums:
         print(num)
     ```

2. **Finding Max / Min**

   * Keep track of the largest/smallest element
   * Example:

     ```python
     max_val = float('-inf')
     for num in nums:
         if num > max_val:
             max_val = num
     print(max_val)
     ```

3. **Prefix Sum Concept**

   * Precompute sums to avoid repeated addition
   * Example:

     ```python
     prefix = [0] * (len(nums) + 1)
     for i in range(len(nums)):
         prefix[i+1] = prefix[i] + nums[i]
     print(prefix)  # prefix[i] = sum of first i elements
     ```

4. **Brute Force vs Optimized Thinking**

   * Always check if **nested loops** can be replaced by **tracking variables** or **prefix sums**.

---

## **Practice Problems (Day 1)**

| Problem                               | Difficulty  | Focus                                            |
| ------------------------------------- | ----------- | ------------------------------------------------ |
| **Two Sum**                           | Easy        | Use hashmap or nested loop, understand iteration |
| **Maximum Subarray (Kadane Preview)** | Easy-Medium | Track max sum ending at current index            |
| **Move Zeroes**                       | Easy        | Array manipulation, in-place swaps               |

---

## **Step-by-Step Example: Maximum Subarray (Kadane’s Idea)**

```python
nums = [-2,1,-3,4,-1,2,1,-5,4]

max_ending_here = nums[0]
max_so_far = nums[0]

for i in range(1, len(nums)):
    max_ending_here = max(nums[i], max_ending_here + nums[i])
    max_so_far = max(max_so_far, max_ending_here)

print(max_so_far)  # Output: 6
```

* **Pattern:** Keep a running max; decide whether to continue or start fresh.

---

## **Tips for Day 1**

1. **Write down what you are tracking** for each problem (state variables).
2. **Dry run examples** on paper to see the flow of your code.
3. Focus on **understanding logic first, then code**.

---

## **Daily Goal**

* Solve **all 3 practice problems**
* Write **1–2 lines explaining the approach** before coding
* Update your **DSA notebook** with patterns observed
