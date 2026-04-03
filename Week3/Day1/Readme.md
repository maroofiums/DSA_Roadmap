# DAY 1 - Two Pointers (Same Direction)

## Goal

Learn how to **modify arrays in-place** using two pointers without extra space.

---

# Core Concept

You use two pointers with **different roles**:

* **Read pointer** → scans every element
* **Write pointer** → decides where to place valid elements

---

# Mental Model (VERY IMPORTANT)

Think like this:

> “I scan everything, but I only write what I want to keep”

---

# Pattern

> Filtering / rearranging → Two Pointers (same direction)

---

# Pointer Roles (Clear Understanding)

## Read Pointer

* Moves through entire array
* Reads every element

## Write Pointer

* Moves only when needed
* Tracks position to place next valid element

---

# Problem 1 - Move Zeroes

## Idea

* You want all non-zero elements at the front
* Zeroes automatically go to the end

### Thinking

* Read pointer → scans all elements
* If element is non-zero:

  * place it at write pointer
  * move write pointer

---

## Key Insight

You are not “moving zeroes”

You are:

> Collecting non-zero elements forward

---

# Problem 2 - Remove Duplicates (Sorted Array)

## Idea

* Array is sorted → duplicates are adjacent
* Keep only unique elements

---

## Thinking

* Read pointer checks each element
* Compare with previous valid element
* If different → write it

---

## Key Insight

> Sorted property allows easy duplicate detection

---

# Problem 3 - Remove Element

## Idea

* Remove all occurrences of a given value

---

## Thinking

* Read pointer scans
* If element ≠ target:

  * write it forward

---

## Key Insight

> Keep only what satisfies condition

---

# Common Pattern Behind All 3

They all follow:

1. Read everything
2. Filter based on condition
3. Write valid elements forward

---

# Visualization (Important)

Example:

```
[0,1,0,3,12]
```

You mentally build:

```
[1,3,12, _, _]
```

---

# Common Mistakes

Do NOT:

* Use extra array (breaks constraint)
* Confuse pointer roles
* Move write pointer incorrectly
* Try to “swap blindly”

---

# When to Use This Pattern

Use same-direction pointers when:

* You need to **filter elements**
* You need **in-place modification**
* Order must be preserved

---

# Mental Checklist (Before Coding)

Ask:

1. Am I filtering elements?
2. Do I need to keep order?
3. Can I overwrite unwanted values?

If YES → Two pointers (same direction)

---

# Task (Do This Properly)

For each problem:

1. Explain:

   * What does read pointer do?
   * What does write pointer do?

2. Dry run manually:

   * Move Zeroes → `[0,1,0,3,12]`
   * Remove Element → `[3,2,2,3], val=3`

3. Answer:

> Why does write pointer move slower than read pointer?

---

# What You Are Building

This is not just arrays.

You are learning:

* In-place transformations
* Memory optimization
* Pointer discipline

---