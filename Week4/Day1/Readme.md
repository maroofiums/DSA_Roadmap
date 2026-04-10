# DAY 1 - Linked List Basics + Traversal

## Goal

Understand:

> How data is connected and how you move through it using pointers

---

# Core Concept

A linked list is NOT continuous memory like an array.

Instead:

> Each node stores:

* value
* reference (pointer) to next node

---

# Mental Model (VERY IMPORTANT)

Think of it like:

```
[5] → [8] → [2] → [7] → None
```

You cannot jump.

You can only move:

> One step at a time using `.next`

---

# Difference from Arrays

| Arrays             | Linked List            |
| ------------------ | ---------------------- |
| Index-based access | Pointer-based access   |
| Random access O(1) | Sequential access O(n) |
| Continuous memory  | Scattered memory       |

---

# Traversal Concept

Traversal means:

> Visit every node one by one

---

# Core Operation

This is the most important line in linked lists:

> current = current.next

---

# What this actually means

* You are currently at one node
* You follow the pointer to the next node
* You move forward in the list

---

# Deep Understanding (IMPORTANT)

When you do:

* `current` → points to node A
* `current.next` → points to node B

After moving:

* `current` now points to B

You have **lost A unless stored elsewhere**

---

# Problem 1 - Print Linked List

## Idea

* Start from head
* Visit each node
* Print its value
* Move forward

---

## Thinking

Loop until:

> current becomes None

---

## Key Insight

End of list is:

> current == None

---

# Problem 2 - Find Length of Linked List

## Idea

* Traverse entire list
* Count each node

---

## Thinking

* Start count = 0
* Move pointer step by step
* Increase count

---

## Key Insight

You cannot know length without traversal

---

# MOST IMPORTANT UNDERSTANDING

## Why traversal is necessary?

Because:

> You don’t know what comes next until you follow the pointer

---

# Common Mistakes

Do NOT:

* Forget to move pointer → infinite loop
* Access `.next` when current is None
* Assume random access like arrays

---

# Mental Drill (VERY IMPORTANT)

Imagine this list:

```
10 → 20 → 30 → 40 → None
```

Answer:

1. Where does `head` point?
2. After 1 move, where is `current`?
3. After 3 moves, where are you?
4. When does loop stop?

---

# Pointer Visualization (Critical Skill)

At every step ask:

* Where am I now?
* What is next?
* What happens if I move?

---

# What You Are Building

This day trains:

* Pointer awareness
* Sequential thinking
* Control over movement

---

# Final Check

You are ready for Day 2 if:

* You understand `current = current.next` fully
* You can mentally traverse any list
* You know when traversal stops

---