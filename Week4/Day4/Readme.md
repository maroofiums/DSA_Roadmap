# DAY 4 - Remove Nth Node from End

## Goal

Remove a node from the end **in one pass**, without calculating length.

---

# Core Concept

Use **two pointers with a fixed gap**.

---

# Pattern

> Distance control between pointers → Two pointers (gap technique)

---

# Core Idea

1. Move first pointer **N steps ahead**
2. Then move both pointers together
3. When first reaches end → second is just before target

---

# Why This Works (IMPORTANT)

By creating a gap of N:

> You align the second pointer exactly at the correct position

---

# Visualization

Example:

```id="t9q4k1"
1 → 2 → 3 → 4 → 5
Remove 2nd from end → remove 4
```

---

## Step 1 - Create gap

Move first pointer N steps:

```id="c6h2w8"
first at 3
second at 1
gap = 2
```

---

## Step 2 - Move both together

Move until first reaches end:

```id="q3n7z5"
first → None  
second → 3
```

---

## Result

Second is just before node to delete:

```id="z8m1p4"
3 → 4 → 5
```

So you remove **4**

---

# Key Insight

You are not counting from the end.

You are:

> Aligning pointers using distance

---

# MOST IMPORTANT PART

## Why move first pointer first?

Because:

> It creates the exact gap needed to locate the target node later

---

# Edge Case (VERY IMPORTANT)

## Removing head

Example:

```id="x5j8v2"
1 → 2 → 3
Remove 3rd from end → remove 1
```

After gap:

* first reaches end
* second is still at head

So:

> You must handle head removal carefully

---

# Mental Model

Think like:

* First pointer = leader
* Second pointer = follower
* Gap between them = N

When leader finishes:

> follower is at correct position

---

# Common Mistakes

Do NOT:

* Forget to move first pointer N steps
* Break the gap while moving
* Ignore edge case (removing head)

---

# When to Use This Pattern

Use gap technique when:

* Problem involves “Nth from end”
* You want one-pass solution
* Length is unknown or expensive to compute

---

# Task (IMPORTANT)

## 1. Explain:

* Why does gap stay constant?
* Why does second pointer reach correct node?

---

## 2. Dry run:

```id="a1b2c3"
1 → 2 → 3 → 4 → 5
n = 3
```

Track:

* first pointer
* second pointer

---

# Final Takeaway

You are learning:

> How to convert a “from end” problem into a forward traversal

---

