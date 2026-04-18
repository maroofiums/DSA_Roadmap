# DAY 2 - Monotonic Stack Introduction

## Goal

Learn one of the most valuable interview patterns:

> Find the next greater / warmer / better element efficiently

This is where stack becomes much more powerful than simple push/pop.

---

# Problem - Daily Temperatures

## Goal

For each day, tell how many days until a warmer temperature.

Example:

```id="u4j6as"
[73,74,75,71,69,72,76,73]
```

Output:

```id="lyqlj4"
[1,1,4,2,1,1,0,0]
```

Meaning:

* 73 waits 1 day for 74
* 75 waits 4 days for 76
* 76 has no warmer future day → 0

---

# Core Concept - Unresolved Elements

Some days do not yet know their answer.

Example:

Today = 73

Question:

> When is the next warmer day?

We don’t know yet.

So this day becomes:

> unresolved

---

# Why Stack Is Used

We store unresolved days in a stack until future temperatures solve them.

---

# MOST IMPORTANT IDEA

The stack stores:

> Indices of days waiting for warmer temperature

Not values only.

---

# Why Indices Are Stored (CRITICAL)

Because answer needs:

> Distance = future_day - current_day

To calculate waiting days, you need positions.

Example:

* day 2 waits until day 5
* answer = 3 days

Temperature alone is not enough.

---

# Core Logic

## When current temperature is warmer than stack top:

That means:

> We found the answer for previous colder day

So pop it and resolve.

---

# Why Popping Happens

Because once answer is found:

> That day no longer needs to stay unresolved

It is finished.

---

# Mental Flow

For each day:

## Step 1

While current temp is warmer than unresolved top day:

* pop previous index
* calculate wait time

## Step 2

Push current day index into stack

(Current day may need future warmer day)

---

# What Is Monotonic Stack?

Here stack is maintained in decreasing temperatures.

Meaning top contains recent unresolved colder/warmer relationship structure.

For Daily Temperatures:

> Temperatures of stored indices are decreasing from bottom to top

---

# Example Dry Run

Input:

```id="k9e1tm"
[73,74,75]
```

---

## Day 0 = 73

No unresolved days before it.

Push index 0

Stack:

```id="jlwm6l"
[0]
```

---

## Day 1 = 74

74 > 73

So day 0 gets answer.

Pop 0

Wait = 1 - 0 = 1

Push day 1

Stack:

```id="z8y6hj"
[1]
```

---

## Day 2 = 75

75 > 74

Pop 1

Wait = 1

Push 2

Stack:

```id="x2n7vw"
[2]
```

---

Final unresolved day gets 0

---

# Deep Insight

You are not comparing every future day.

You are letting future days resolve waiting past days.

That is why this becomes efficient.

---

# Why This Beats Brute Force

Brute force:

For every day, search ahead.

O(n²)

Monotonic stack:

Each index pushed once, popped once.

O(n)

---

# Common Mistakes

Do NOT:

* Store only temperatures (lose positions)
* Forget multiple pops
* Push before resolving
* Think stack stores answers

---

# Pattern Recognition

Use monotonic stack when you hear:

* Next greater element
* Next warmer day
* Previous smaller
* Future better value

---

# Mental Checklist

Ask:

1. Need next greater/smaller?
2. Need nearest future answer?
3. Brute force compares too much?

If YES → monotonic stack

---

# Task (IMPORTANT)

Dry run:

```id="7p49yt"
[30,40,35,50]
```

Track:

* stack indices
* pops
* answers

---

# Final Takeaway

This pattern teaches:

> Keep unresolved items in stack until future data solves them.

---