# Day 1 — Linked List Fundamentals

## 1. What is a Linked List

A **Linked List** is a chain of nodes.

Each node contains:

* **value**
* **pointer to next node**

Conceptually:

```
[5 | next] → [8 | next] → [12 | next] → None
```

Key difference from arrays:

| Array              | Linked List        |
| ------------------ | ------------------ |
| Contiguous memory  | Scattered memory   |
| Index access O(1)  | Traversal required |
| Easy random access | Easy insertion     |

---

# 2. Traversal

Traversal means **visiting every node**.

Idea:

```
current = head

while current:
    visit node
    current = current.next
```

Pointer moves **node → node → node**

Important mindset:

```
You NEVER jump in linked list
You only follow pointers
```

---

# 3. Reversing a Linked List

Original list:

```
1 → 2 → 3 → 4 → None
```

Reversed list:

```
4 → 3 → 2 → 1 → None
```

### Core Idea

We **flip the direction of pointers**.

Normal:

```
1.next → 2
```

After reverse:

```
2.next → 1
```

To do this safely we need **3 pointers**:

```
prev
curr
next
```

Visualization:

```
prev ← curr → next
```

Step logic:

1. Save next node
2. Reverse current pointer
3. Move prev forward
4. Move curr forward

Mental model:

```
curr.next = prev
prev = curr
curr = next
```

---

# 4. Iterative vs Recursive Reverse

### Iterative

We manually move pointers.

Advantages:

* Faster
* Uses O(1) memory

---

### Recursive

Idea:

```
reverse rest of list
attach current node at end
```

Conceptually:

```
reverse(1→2→3→4)

→ reverse(2→3→4)
→ reverse(3→4)
→ reverse(4)
```

Then reconnect.

---

# 5. Detecting Cycle in Linked List

Problem:

```
1 → 2 → 3 → 4
      ↑     ↓
      ← ← ←
```

A node points back → **cycle**

---

# Floyd's Tortoise & Hare Algorithm

Use **two pointers**.

```
slow = 1 step
fast = 2 steps
```

Visualization:

```
slow: 1 → 2 → 3 → 4
fast: 1 → 3 → 1 → 3
```

If there is a cycle:

```
fast will eventually catch slow
```

Key Rule:

```
If slow == fast → cycle exists
```

If list ends:

```
fast reaches None → no cycle
```

---

# Why This Works (Important Intuition)

Inside a cycle:

Fast moves **twice as fast**.

So distance between them **shrinks every step**.

Eventually:

```
fast catches slow
```

Same idea as **two runners on a circular track**.

---

# Pattern Recognition

When you see:

```
Linked List
Cycle
Loop detection
Middle node
```

Think immediately:

```
Fast and Slow pointers
```

---

# Problems You Solve Today

### 1️⃣ Reverse Linked List

Goal:

* Understand pointer manipulation.

Pattern:

```
prev
curr
next
```

---

### 2️⃣ Linked List Cycle

Goal:

* Detect loops efficiently.

Pattern:

```
slow += 1
fast += 2
```

---

# What Mastery Looks Like

After today you should be able to answer instantly:

* Why we need `prev` in reverse
* How pointers move
* Why fast/slow detects cycles
* When to use this pattern

---

