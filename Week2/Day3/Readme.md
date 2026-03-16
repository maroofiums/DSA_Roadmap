# Day 3 — HashMap Patterns

## 1. What is a HashMap?

A **HashMap (dictionary)** stores data as:

```
key → value
```

Example:

```
{
  "apple": 3,
  "banana": 2,
  "orange": 5
}
```

Access time is usually **O(1)**.

Meaning:

* insert → O(1)
* lookup → O(1)
* update → O(1)

This is why it is powerful in interviews.

---

# 2. Pattern 1 — Frequency Counting

### Idea

Count how many times each element appears.

Example array:

```
[1,1,2,3,3,3,4]
```

HashMap becomes:

```
1 → 2
2 → 1
3 → 3
4 → 1
```

### When to Use

If the problem says:

* count occurrences
* most frequent element
* group similar items

➡ **Use frequency map**

---

# 3. Pattern 2 — Duplicate Detection

### Idea

While traversing the array, check if an element already exists in the HashMap.

Example:

```
[1,2,3,4,2]
```

Steps:

```
1 → not seen → add
2 → not seen → add
3 → not seen → add
4 → not seen → add
2 → already exists → duplicate found
```

### When to Use

If the problem asks:

* detect duplicates
* unique elements
* first unique character

---

# 4. Pattern 3 — Complement Lookup (Two Sum)

This is **one of the most famous interview patterns**.

Example:

```
nums = [2,7,11,15]
target = 9
```

Instead of checking every pair (O(n²)):

Idea:

```
target - current_number = complement
```

Steps:

```
2 → need 7 → store 2
7 → need 2 → found → answer
```

HashMap stores numbers we already saw.

Time complexity:

```
O(n)
```

Instead of:

```
O(n²)
```

---

# 5. Pattern 4 — Tracking Counts

Sometimes we track counts **while traversing**.

Example:

```
Top K Frequent Elements
```

Steps:

1. Count frequency using HashMap
2. Select top k elements

This combines:

* **HashMap**
* **Heap / Sorting**

---

# 6. How HashMap Replaces Nested Loops

Brute force approach:

```
for i:
   for j:
```

Time complexity:

```
O(n²)
```

Optimized approach:

```
one loop + hashmap lookup
```

Time complexity:

```
O(n)
```

This is one of the **most common interview optimizations**.

---

# Practice Problems Today

### 1. Two Sum

Pattern:

```
Complement Lookup
```

---

### 2. Top K Frequent Elements

Pattern:

```
Frequency Map + Heap / Sorting
```

---

# Key Interview Signals

If the question says:

| Clue in Problem | Use Pattern       |
| --------------- | ----------------- |
| duplicates      | HashSet / HashMap |
| frequency       | HashMap counter   |
| pair sum        | complement lookup |
| top frequent    | frequency + heap  |

---

# Target for Today

Time goal:

| Problem        | Target Time |
| -------------- | ----------- |
| Two Sum        | 10 minutes  |
| Top K Frequent | 25 minutes  |

Total:

**~35 minutes**

---
