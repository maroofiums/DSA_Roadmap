# DAY 6 - Pattern Mastery (Stack + Queue)

## Goal

Move from “I can solve it” → to:

> “I instantly recognize the pattern and simulate it in my head”

No code. Only understanding + dry runs.

---

# 1. Valid Parentheses

## Pattern

Matching Stack

---

## Idea

You use a stack to track **unmatched opening brackets**.

---

## Why stack works

Because:

> The last opened bracket must close first (LIFO rule)

---

## Mental Process

* Opening bracket → store it
* Closing bracket → must match most recent opening

If mismatch → invalid immediately

---

## Dry run idea

Example:

```
([{}])
```

Stack evolves:

* (
* ([
* ([{
* match } → pop
* match ] → pop
* match ) → pop

Final: empty → valid

---

# 2. Daily Temperatures

## Pattern

Monotonic Stack (Next Greater Element)

---

## Idea

We store **indices of unresolved days** waiting for a warmer future day.

---

## Why stack works

Because:

> We want next greater element efficiently without checking all future days

---

## Key Behavior

When a warmer day comes:

* It resolves multiple previous colder days at once

---

## Dry run idea

```
[73, 74, 75]
```

* 73 waits
* 74 resolves 73
* 75 resolves 74

Each element handled once

---

# 3. Min Stack

## Pattern

Design + State Tracking

---

## Idea

Each stack entry stores:

> value + minimum so far

---

## Why it works

Because:

> You are precomputing answers while inserting

No recalculation needed later.

---

## Mental Flow

At each push:

* compare current value with previous min
* store updated min

At pop:

* previous min automatically restored

---

## Dry run idea

```
Push: 4 → min 4  
Push: 2 → min 2  
Push: 5 → min 2  
Pop 5 → min still 2  
Pop 2 → min becomes 4
```

---

# 4. Next Greater Element

## Pattern

Monotonic Stack

---

## Idea

We maintain a stack of **unresolved elements**.

---

## Why popping happens

When a bigger number arrives:

> It becomes the answer for smaller previous elements

So those elements are resolved and removed.

---

## Dry run idea

```
[2, 1, 3]
```

* 2 waits
* 1 waits
* 3 resolves both 1 and 2

---

# 5. Queue Tasks

## Pattern

FIFO (First In First Out)

---

## Idea

Order matters strictly:

> First arrived → processed first

---

## Why queue works

Because:

> We are modeling real-world order systems

---

## Mental Examples

* people in line
* task scheduling
* BFS traversal (future topic)

---

## Dry run idea

```
Enqueue: 1, 2, 3  
Dequeue: 1 → 2 → 3
```

---

# BIG PATTERN SUMMARY

| Problem            | Pattern         | Core Idea                |
| ------------------ | --------------- | ------------------------ |
| Valid Parentheses  | Matching stack  | Reverse nesting order    |
| Daily Temperatures | Monotonic stack | Next greater in future   |
| Min Stack          | Design          | Track min continuously   |
| Next Greater       | Monotonic stack | Resolve past with future |
| Queue tasks        | FIFO            | Preserve arrival order   |

---

# FINAL MASTER CHECK

You should instantly answer:

## Q1

Why stack for parentheses?

→ Because of reverse matching order

---

## Q2

Why monotonic stack?

→ To avoid rechecking future elements

---

## Q3

Why min stack works?

→ Because state is stored at each step

---

## Q4

Why queue?

→ Because processing order must be preserved

---

# FINAL TAKEAWAY

You are learning:

> How to choose data structure based on “order behavior”

Not memorizing solutions.