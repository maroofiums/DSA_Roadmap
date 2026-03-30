# DAY 3 - Sliding Window (Longest Substring Without Repeating)

## Concept

Instead of checking all substrings (brute force), you maintain a **window**:

* Expand → include new characters
* Shrink → remove characters when condition breaks

---

# Problem Understanding

## Goal

Find the **longest substring** where:

> No character repeats

---

# Core Idea

You maintain a window `[left → right]` such that:

* All characters inside are **unique**
* If duplicate appears → fix it immediately

---

# Pattern

> Substring + constraint → Sliding Window

Constraint here:

> “No repeating characters”

---

# How Your Brain Should Think

You don’t restart every time.

You **adjust the window dynamically**.

---

# Step-by-Step Thinking

You have two pointers:

* `left` → start of window
* `right` → end of window

You also track:

* characters inside window (using set/map)

---

# Algorithm Flow (Conceptual)

1. Start with empty window
2. Move `right` forward (expand)
3. If character is new → continue
4. If duplicate found:

   * Move `left` forward (shrink)
   * Remove characters until duplicate is gone
5. Keep updating max length

---

# Dry Run (VERY IMPORTANT)

Example:

```
"abcabcbb"
```

## Step-by-step window movement

| Step           | Window    | Action           |
| -------------- | --------- | ---------------- |
| a              | a         | expand           |
| b              | ab        | expand           |
| c              | abc       | expand           |
| a              | duplicate | shrink from left |
| window becomes | bca       | continue         |
| b              | duplicate | shrink           |
| c              | duplicate | shrink           |

Max length = **3 ("abc")**

---

# Key Insight (MOST IMPORTANT)

Why shrink?

> Because once duplicate appears, current window becomes invalid

So instead of restarting:

* You **fix the window**
* This avoids O(n²)

---

# Mental Model

Think like this:

> “I maintain a valid window at all times”

* Expand → try to grow
* Shrink → fix violations

---

# Common Mistakes

Do NOT:

* Restart from next index (that’s brute force)
* Forget to remove elements when shrinking
* Move both pointers randomly

---

# What You Are Learning Here

This pattern teaches:

* Efficient range processing
* Dynamic condition maintenance
* Optimization from O(n²) → O(n)

---

# Task (Do This Seriously)

## 1. Dry run manually:

```
"pwwkew"
```

Track:

* left
* right
* window content

---

## 2. Answer this (very important)

Why don’t we reset everything when duplicate appears?

---

## 3. Pattern recognition

If problem says:

* “longest substring”
* “no duplicates”
* “at most k distinct”

What pattern?

→ Sliding Window

---
