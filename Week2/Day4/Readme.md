# Day 4 — HashMap + Prefix Sum

## 1. Prefix Sum Concept

Prefix sum means **running total while traversing the array**.

Example:

Array

```
[1, 2, 3, 4]
```

Prefix sums become

```
1
1+2 = 3
3+3 = 6
6+4 = 10
```

So the prefix array is

```
[1, 3, 6, 10]
```

Key idea:

If we know prefix sums, we can compute **any subarray sum quickly**.

Subarray sum from index **i to j**

```
sum(i,j) = prefix[j] - prefix[i-1]
```

---

# 2. Prefix Sum + HashMap Pattern

Instead of checking **all subarrays** (which is O(n²)), we store **previous prefix sums in a HashMap**.

### Core Formula

If we want a subarray with sum = **target**

We check:

```
previous_prefix = current_sum - target
```

If that prefix exists in the hashmap → we found a valid subarray.

---

### Example

Array

```
[1, 2, 3]
target = 3
```

Steps:

```
current_sum = 1
need = 1 - 3 = -2 → not found

current_sum = 3
need = 3 - 3 = 0 → found
```

This means subarray:

```
[1,2]
```

---

### HashMap Stores

```
prefix_sum → frequency
```

Example

```
{
0 : 1
1 : 1
3 : 1
}
```

---

# 3. Sliding Window + HashMap

Sliding window is used mainly for **strings or positive numbers**.

Idea:

Instead of checking every substring:

```
start
end
```

We expand and shrink the window.

Example:

```
abcabcbb
```

Goal: longest substring without repeating characters.

Window expands:

```
a
ab
abc
```

When duplicate appears:

```
abca
```

We **shrink from the left** until the duplicate disappears.

HashMap stores:

```
character → index
```

---

# 4. Problem 1 — Subarray Sum Equals K

Pattern used:

```
Prefix Sum + HashMap
```

Key insight:

Instead of checking all subarrays:

```
for i
   for j
```

We check:

```
current_sum - k
```

If it exists in hashmap → valid subarray.

Time complexity

```
O(n)
```

---

# 5. Problem 2 — Minimum Window Substring

Pattern used:

```
Sliding Window + HashMap
```

Idea:

We maintain a window that **contains all required characters**.

Steps:

1. Expand window (move right pointer)
2. Track character counts
3. When valid window found → shrink from left
4. Keep the **minimum window**

HashMap stores:

```
character → required frequency
```

---

# 6. When to Recognize These Patterns

### Use Prefix Sum + HashMap when:

Problem mentions:

* **subarray sum**
* **number of subarrays**
* **target sum**

---

### Use Sliding Window + HashMap when:

Problem mentions:

* **substring**
* **longest / shortest window**
* **characters frequency**

---

# Key Pattern to Remember

Instead of checking all subarrays:

```
O(n²)
```

We store prefix sums.

Then check

```
previous_prefix = current_sum - target
```

This reduces complexity to

```
O(n)
```

---

# Your Practice Today

Solve:

1. **Subarray Sum Equals K**
   Target time: **25 minutes**

2. **Minimum Window Substring**
   Target time: **35 minutes**

These are **very common interview questions**.

