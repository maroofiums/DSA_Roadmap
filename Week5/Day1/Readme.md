# DAY 1 - Stack Basics + Valid Parentheses

## Goal

Understand **why stack exists** and how push/pop solves ordering problems.

---

# Core Concept - Stack

Stack follows:

> Last In, First Out (LIFO)

Meaning:

* Last item added comes out first

---

# Real-Life Example

Think of plates stacked vertically:

* Put new plate on top
* Remove plate from top

You cannot remove middle plate first.

---

# Operations

## Push

Add item to top.

## Pop

Remove top item.

## Peek / Top

See top item without removing.

---

# Why Stack Is Powerful

Stack is useful when problem depends on:

* recent history
* nested structure
* reverse order
* matching pairs

---

# Problem - Valid Parentheses

## Goal

Check if brackets are correctly opened and closed.

Examples:

Valid:

```id="q6t5po"
()
([]){}
```

Invalid:

```id="tvdkyd"
(]
([)]
((
```

---

# Core Idea

## Rule 1

Every opening bracket:

* `(`
* `[`
* `{`

gets stored in stack.

Why?

> Because it is waiting for a future match.

---

## Rule 2

Every closing bracket:

* `)`
* `]`
* `}`

must match the **most recent unmatched opening bracket**.

That means:

> It must match stack top.

---

# Why Top Element Matters (MOST IMPORTANT)

Example:

```id="xj84m0"
([ ])
```

Openings happened in order:

1. `(`
2. `[`

So closing must happen in reverse:

1. `]`
2. `)`

Why?

Because `[` was opened last.

That is exactly LIFO.

---

# This Is the Deep Insight

Nested structures close in reverse order.

So:

> Stack naturally models nesting.

---

# Example Dry Run

## Input:

```id="t6if0n"
([])
```

### Step 1

Read `(`
→ push

Stack:

```id="4j6gxj"
(
```

### Step 2

Read `[`
→ push

Stack:

```id="s50q8k"
( [
```

### Step 3

Read `]`

Must match top = `[`
Correct → pop

Stack:

```id="3ij0vg"
(
```

### Step 4

Read `)`

Must match top = `(`
Correct → pop

Stack empty → valid

---

# Invalid Example

## Input:

```id="p8h0g6"
([)]
```

Open:

* `(`
* `[`

Then read `)`

Top is `[` not `(`

Mismatch.

Invalid immediately.

---

# Common Mistakes

Do NOT:

* Match with any earlier bracket
* Ignore order
* Forget empty stack case

Example:

```id="1n1ujp"
)
```

No opening exists.

Invalid.

---

# Pattern Recognition

Use stack when you see:

* parentheses
* brackets
* nested expressions
* matching open/close symbols

---

# Mental Checklist

When reading a symbol:

## If opening:

> Save it for later

## If closing:

> Must match most recent opening

---

# What You’re Really Learning

Not just brackets.

You’re learning:

> How to track unfinished work using stack.

This pattern appears everywhere.

---

# Task (IMPORTANT)

Dry run manually:

1.

```id="p9a6j0"
()[]{}
```

2.

```id="8mx29g"
([{}])
```

3.

```id="26ygd1"
(]
```

For each step, write stack state.

---

# Final Takeaway

Stack solves this because:

> The last opened bracket must close first.

That is LIFO.

---