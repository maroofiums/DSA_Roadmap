# Week 1 — Day 5: Two Pointer Pattern

## **Goal**

Understand **the two pointer pattern** and when to apply it. This is a **core pattern** for arrays and strings, especially **sorted arrays**.

---

## **Concept**

Two pointers are **indices that move in the array simultaneously**:

* One pointer usually starts at the **beginning** (`left`)
* One pointer starts at the **end** (`right`)

**Idea:** Move pointers toward each other based on conditions to **reduce search space**.

### **When to use**

* The array (or string) is **sorted**.
* You are looking for **pairs or triplets** that satisfy a condition.
* You want **O(n) solution instead of O(n²)**.

### **Common Variations**

1. **Sum / Difference Problems**

   * Example: Find two numbers that sum to a target.
   * Start with `left = 0` and `right = len-1`
   * Move pointers **based on sum comparison**:

     * Sum too small → move left forward
     * Sum too large → move right backward

2. **Container / Max Area Problems**

   * Example: Container with Most Water
   * Keep **max area** tracked
   * Move the pointer pointing to the **smaller value** inward

3. **Triplets or Multiple Pointers**

   * Example: 3Sum
   * Fix one number, then apply **two pointers** on the remaining subarray

---

## **Practice Problems (Ideas Only)**

1. **Two Sum II (Sorted Array)**

   * Given a sorted array, find two numbers whose sum equals a target.
   * Use two pointers to efficiently find the pair without nested loops.

2. **Container With Most Water**

   * Find the **maximum area** formed by two lines in an array of heights.
   * Use two pointers and always **move the pointer with smaller height**.

3. **3Sum**

   * Find triplets that sum to zero.
   * Sort array first → fix one element → use two pointers for remaining elements.

---

## **Key Ideas / Patterns**

* Always **sort first** if input isn’t sorted.
* **Decide pointer movement** based on **current condition**.
* Can be combined with **sliding window** for some substring/subarray problems.
* Works best for **pair/triplet problems** in sorted arrays.

---

## **Daily Success Criteria**

After Day 5, you should be able to:

* Identify when **two pointer pattern** is needed
* Explain **pointer movement logic** without writing code
* Solve array problems in **O(n)** that would otherwise take **O(n²)**

---