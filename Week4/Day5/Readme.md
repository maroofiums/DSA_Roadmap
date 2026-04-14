# DAY 5 - Merge Two Sorted Lists

## Goal

Learn how to **combine two linked structures using pointer traversal** while maintaining order.

---

# Core Concept

You are not “sorting” anything.

You are:

> Building a new sorted list by comparing two already sorted lists

---

# Pattern

> Parallel traversal + greedy choice → Merge using pointers

---

# Core Idea

At every step:

* Compare current nodes of both lists
* Take the smaller value
* Move that pointer forward
* Attach node to result list

---

# Mental Model

Think like:

> Two sorted queues → always pick smallest front element

---

# Step-by-Step Thinking

## Step 1 - Compare

Look at:

* node from list 1
* node from list 2

---

## Step 2 - Choose

Pick the smaller node:

* it becomes next in result list

---

## Step 3 - Move Pointer

Advance pointer of the list you used

---

## Step 4 - Repeat

Continue until one list ends

---

# Key Insight

You are always making a **locally optimal choice**:

> smallest available node

---

# Handling Remaining Nodes

When one list finishes:

* The other list is already sorted
* So just attach it directly

---

# Why This Works

Because both lists are already sorted:

> You only need to decide the next smallest element

No re-sorting needed.

---

# Visualization Idea

Imagine two sorted lines:

```
List A: 1 → 3 → 5  
List B: 2 → 4 → 6
```

You are building:

```
1 → 2 → 3 → 4 → 5 → 6
```

By always picking the smallest front node.

---

# Important Concept

This is NOT:

* merging randomly
* rebuilding entire structure

It is:

> controlled pointer traversal with comparisons

---

# Common Mistakes

Do NOT:

* Forget to move pointer after choosing node
* Lose reference to remaining nodes
* Try to compare full lists repeatedly (inefficient thinking)

---

# Edge Cases

## 1. One list empty

* Return other list directly

## 2. Different lengths

* Attach remaining part as-is

---

# When to Use This Pattern

Use it when:

* Two sorted lists/arrays exist
* You need combined sorted output
* You want efficient O(n + m) solution

---

# Mental Checklist

Before coding, ask:

1. Are both inputs sorted?
2. Can I choose elements greedily?
3. Do I only need local comparison?

If YES → merge pattern

---

# Big Insight of Day 5

You are learning:

> How to build sorted structure using only comparisons, not sorting logic

---

# Task (IMPORTANT)

## 1. Explain:

* Why greedy choice works here?
* Why no backtracking is needed?

---

## 2. Dry run:

```
1 → 4 → 7  
2 → 3 → 6
```

Track:

* comparisons
* pointer movement

---

# Final Takeaway

This pattern teaches:

> Building complex structures step-by-step using local decisions

---
