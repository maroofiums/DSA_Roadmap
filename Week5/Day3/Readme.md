# DAY 3 - Design Stack Problem

## Goal

Learn how to make a stack **smarter**, not just store values.

You’ll learn:

> How to retrieve minimum value in O(1) time

This is a classic **design + data structure thinking** problem.

---

# Problem - Min Stack

## Required Operations

Support all efficiently:

* Push(x)
* Pop()
* Top()
* GetMin()

And:

> GetMin() must be O(1)

---

# Normal Stack Problem

A regular stack can do:

* push → O(1)
* pop → O(1)
* top → O(1)

But:

> Finding minimum normally requires scanning everything → O(n)

That is too slow.

---

# Core Concept

You need **parallel state tracking**.

Meaning:

> While storing values, also store minimum information.

---

# Big Idea

Whenever stack changes, minimum status must also update instantly.

So instead of searching later:

> Maintain the answer continuously.

---

# Two Ways to Think

## Method 1 - Separate Min Tracking Stack

One stack stores values.
Another stack stores current minimums.

---

## Method 2 - Pair Storage

Each pushed item stores:

* value
* minimum so far

Example:

```id="n7cbv4"
(5,5)
(3,3)
(7,3)
(2,2)
```

Meaning:

* top value = first part
* min so far = second part

---

# Why This Works

At every level of stack:

> You already know the minimum up to that point

So `getMin()` is just top’s stored minimum.

No searching needed.

---

# O(1) Retrieval Logic

Instead of:

“Find min now”

You do:

> “I already kept track while pushing”

---

# Example Dry Run

Push 5

Stack:

```id="h6a5ql"
(5,5)
```

---

Push 3

```id="n3ur18"
(5,5)
(3,3)
```

---

Push 7

```id="5q7s7p"
(5,5)
(3,3)
(7,3)
```

Current min = 3

---

Push 2

```id="8kzjpn"
(5,5)
(3,3)
(7,3)
(2,2)
```

Current min = 2

---

Pop 2

Top becomes:

```id="f3o4rz"
(7,3)
```

Current min automatically returns to 3

---

# Deep Insight

You are storing:

> History of minimum values

So when top is removed, previous minimum is restored instantly.

---

# Why This Is a Design Problem

Because interviewer tests:

* Can you augment a data structure?
* Can you preserve efficiency?
* Can you track metadata?

---

# Common Mistakes

Do NOT:

* Recalculate min on every query
* Store only one global min without history
* Forget duplicates of minimum values

Example:

Push:

```id="ziv6fv"
2,2,3
```

Pop one 2 later → still need another 2 remembered.

---

# Pattern Recognition

Use this thinking when asked:

* Support fast max/min queries
* Custom stack behavior
* O(1) extra retrieval operations

---

# Mental Model

Think:

Normal stack stores values.

Smart stack stores:

* values
* useful state about past values

---

# Task (IMPORTANT)

Dry run:

Push:

```id="e0x5s0"
4,1,6,1
```

Then pop twice.

At each step answer:

* top?
* min?

---

# Final Takeaway

This problem teaches:

> Great systems are fast because they maintain state continuously.

Not because they recompute later.
