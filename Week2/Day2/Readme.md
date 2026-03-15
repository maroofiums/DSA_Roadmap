# Day 2 — Linked List Manipulation

## 1. Finding the Middle Node

### Idea

Instead of counting the length first, we use **two pointers**.

* **Slow pointer** → moves **1 step**
* **Fast pointer** → moves **2 steps**

When the fast pointer reaches the end, the slow pointer will be at the **middle**.

### Why it Works

Fast moves twice as fast as slow.
So when fast finishes the list, slow has only traveled **half the distance**.

### Visualization

Example:

List
1 → 2 → 3 → 4 → 5

Movement:

| Step  | Slow  | Fast |
| ----- | ----- | ---- |
| Start | 1     | 1    |
| 1     | 2     | 3    |
| 2     | 3     | 5    |
| End   | **3** | None |

Middle = **3**

### Pattern Recognition

If the problem says:

* middle element
* split list
* check palindrome

➡ **Fast / Slow pointer**

---

## 2. Merge Two Sorted Lists

### Problem Idea

You are given two **sorted linked lists**.

Example:

List A
1 → 3 → 5

List B
2 → 4 → 6

Goal:

1 → 2 → 3 → 4 → 5 → 6

### Key Idea

Compare nodes **one by one** and attach the smaller value to the new list.

### Important Trick — Dummy Node

Instead of worrying about the first node, we create a **dummy head**.

Dummy → ?

Then we build the list after it.

Example:

Dummy → 1 → 2 → 3 → 4 → 5 → 6

Finally return:

```
dummy.next
```

### Why Dummy Node Helps

Without dummy:

* first node handling becomes messy

With dummy:

* logic stays **clean and consistent**

---

## 3. Merge K Sorted Lists (Concept Only)

This is a **harder version** of merge two lists.

Instead of 2 lists:

```
List1
List2
List3
...
ListK
```

### Three Common Approaches

#### 1️⃣ Brute Force

Collect all values → sort → rebuild list

Time complexity
**O(N log N)**

Not optimal.

---

#### 2️⃣ Sequential Merge

Merge lists one by one.

```
((L1 + L2) + L3) + L4 ...
```

Time complexity
**O(KN)**

Better but still slow.

---

#### 3️⃣ Optimal — Min Heap

Put first node of each list in a **min heap**.

Always extract the smallest node.

Time complexity

```
O(N log K)
```

This is the **interview-preferred approach**.

---

# Key Tricks to Remember Today

### 1️⃣ Fast Slow Pointer

Used for:

* middle node
* cycle detection
* palindrome linked list

---

### 2️⃣ Dummy Node

Used when:

* building new linked lists
* merging lists
* removing nodes

---

### 3️⃣ Pointer Safety

Always check:

```
node != None
node.next != None
```

Many bugs in linked lists come from **null pointer errors**.

---

# Your Practice Today

Solve these **without looking at solutions**:

1️⃣ Middle of Linked List
2️⃣ Merge Two Sorted Lists
3️⃣ Try to understand idea of **Merge K Sorted Lists**

Target time:

* Middle node → **10 minutes**
* Merge lists → **20 minutes**
* Merge K concept → **15 minutes**

---
