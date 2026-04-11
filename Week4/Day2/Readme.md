# DAY 2 - Reverse Linked List

## Goal

Learn how to **change direction of links safely** without losing data.

---

# Core Concept

Originally:

```id="9l2c8v"
1 → 2 → 3 → 4 → None
```

After reversal:

```id="8g6q0r"
1 ← 2 ← 3 ← 4 ← None
```

But since linked lists are one-directional, it becomes:

```id="1f6v9k"
4 → 3 → 2 → 1 → None
```

---

# The Real Problem

Each node only knows its **next**.

When you reverse:

> You are breaking the original connection and creating a new one

---

# 3 Pointers (MANDATORY)

You must track:

* **current** → node you are processing
* **previous** → node that comes before (new direction)
* **next** → to avoid losing the rest of list

---

# Core Idea

At each step:

> Take current node and reverse its pointer

---

# Mental Flow (CRITICAL ORDER)

## Step 1 - Save next

Why?

> Because once you reverse, you lose access to the rest of list

---

## Step 2 - Reverse link

Make:

* current.next → point to previous

---

## Step 3 - Move forward

* previous → becomes current
* current → moves to next

---

# MOST IMPORTANT RULE

> If you don’t save next, you lose the entire remaining list

---

# Visualization (Step-by-Step Thinking)

Start:

```id="9l5t3r"
prev = None
curr = 1 → 2 → 3 → 4
```

---

## Iteration 1

* Save next (2)
* Reverse: 1 → None
* Move pointers

Now:

```id="n3wr9h"
prev = 1
curr = 2 → 3 → 4
```

---

## Iteration 2

* Save next (3)
* Reverse: 2 → 1
* Move

Now:

```id="v2x8qs"
prev = 2 → 1
curr = 3 → 4
```

---

Continue until `curr = None`

Final:

```id="l7m2az"
prev = 4 → 3 → 2 → 1
```

---

# Key Insight

You are not “reversing the list”

You are:

> Rebuilding it one node at a time in reverse direction

---

# Why Order Matters

Wrong order = data loss

Correct order:

1. Save next
2. Reverse
3. Move

---

# Common Mistakes

Do NOT:

* Reverse before saving next
* Forget to move pointers
* Lose reference to remaining list

---

# Mental Model

Think like this:

* You are cutting links
* Then reconnecting them backward

---

# When You Master This

You unlock:

* Reverse in K groups
* Palindrome linked list
* Reorder list
* Many advanced problems

---

# Task (VERY IMPORTANT)

You should be able to:

## 1. Explain:

* Why do we need 3 pointers?
* What happens if we don’t store next?

## 2. Dry run:

```id="r0v0gi"
1 → 2 → 3
```

Step by step without confusion

---

# Final Check

You are ready if:

* You can simulate reversal in your head
* You never lose track of nodes
* You understand pointer movement clearly

---