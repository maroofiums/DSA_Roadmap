# Week 1 — Day 6: Sliding Window Pattern

## **Goal**

Master the **sliding window pattern** for **subarray and substring problems**. This is one of the most common and powerful patterns in interviews.

Daily target: **3–4 problems**

---

## **Concept**

Instead of checking **all subarrays (O(n²))**, we maintain a **window** that represents a valid subarray/substring:

* **Expand the window** by moving the right pointer
* **Shrink the window** by moving the left pointer when a condition is violated

**Pattern:**

* The **window size** can be **fixed** or **variable** depending on the problem.
* We keep track of **state variables** (e.g., count of unique characters, sum, max/min) inside the window.

---

## **When to Use**

* Finding **longest / shortest** subarray or substring that satisfies a condition
* Counting **subarrays / substrings** with a property
* Problems where **nested loops** are too slow

---

## **Common Variations**

1. **Longest / Shortest Substring without Repeating Characters**

   * Expand window until a duplicate appears
   * Shrink left pointer until all characters are unique again

2. **Minimum Size Subarray Sum**

   * Expand right pointer to include elements
   * Shrink left pointer once sum ≥ target

3. **Longest Repeating Character Replacement**

   * Maintain count of most frequent character in window
   * Expand window while allowed replacements ≤ k
   * Shrink window when condition breaks

---

## **Practice Problems (Ideas Only)**

1. **Longest Substring Without Repeating Characters**

   * Keep a hashmap of characters and their last seen index
   * Move left pointer to remove duplicates

2. **Minimum Size Subarray Sum**

   * Keep a running sum of the window
   * Shrink left pointer when sum ≥ target

3. **Longest Repeating Character Replacement**

   * Keep track of frequency of characters in the window
   * Slide the window and adjust left when needed

---

## **Key Ideas / Patterns**

* **Two pointers + condition checking** = sliding window
* **Window can grow or shrink dynamically**
* Always **update result** (max, min, count) **after each expansion**
* Use **hashmap or array** to track state inside the window

---

## **Daily Success Criteria**

After Day 6, you should be able to:

* Recognize **sliding window problems instantly**
* Explain how to **expand and shrink the window** without nested loops
* Solve substring/subarray problems in **O(n)** instead of **O(n²)**

---
