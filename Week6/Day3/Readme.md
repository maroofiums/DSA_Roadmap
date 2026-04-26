# 🔵 DAY 3 - Rotated Sorted Array Pattern

Today you learn one of the most famous interview questions.

This tests whether you **understand binary search deeply**, not just memorize it.

---

# 🎯 Goal

Solve binary search problems when array is rotated.

Example:

```python id="jz2m4a"
[4,5,6,7,0,1,2]
```

Originally sorted:

```python id="g2h9we"
[0,1,2,4,5,6,7]
```

Then rotated.

---

# 🧠 Core Insight

Even though full array is not sorted...

> **At least one half is always sorted**

This is the secret.

---

# Example

```python id="rz7wke"
[4,5,6,7,0,1,2]
 left      mid     right
```

Mid = 7

Left half:

```python id="u7d4tp"
[4,5,6,7]
```

Sorted ✅

Right half:

```python id="p8v1qo"
[0,1,2]
```

Not needed now.

---

# 🔥 Main Strategy

Every loop:

1. Find mid
2. Detect which half is sorted
3. Check if target lies in sorted half
4. Go there
5. Else go other half

---

# 🧩 How to Detect Sorted Half

If:

```python id="9t4ykm"
nums[left] <= nums[mid]
```

Then left half sorted.

Else:

Right half sorted.

---

# 🔍 Problem 33 - Search in Rotated Sorted Array

## Input

```python id="y1d8jk"
nums = [4,5,6,7,0,1,2]
target = 0
```

Output:

```python id="m2q9zt"
4
```

---

# ✅ Clean Code

```python id="x7p3nh"
def search(nums, target):
    left, right = 0, len(nums)-1

    while left <= right:
        mid = (left + right)//2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            # left half sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # right half sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
```

---

# 🧠 Dry Run

```python id="jq9s0m"
nums = [4,5,6,7,0,1,2]
target = 0
```

---

### Step 1

```python id="f3t7po"
left=0 right=6
mid=3 -> 7
```

Check:

```python id="b1v4wr"
nums[left] <= nums[mid]
4 <= 7 ✅
```

Left half sorted.

Does target 0 lie in:

```python id="9u2kdc"
[4 ... 7]
```

No.

Go right:

```python id="u4h7qe"
left = mid + 1 = 4
```

---

### Step 2

```python id="j5n1as"
left=4 right=6
mid=5 -> 1
```

Check:

```python id="p0c8yu"
nums[left] <= nums[mid]
0 <= 1 ✅
```

Left half sorted.

Does target 0 lie in:

```python id="s8m2fv"
[0 ... 1)
```

Yes.

Go left:

```python id="n7d5xt"
right = mid - 1 = 4
```

---

### Step 3

```python id="e2k6bo"
left=4 right=4
mid=4 -> 0
```

Found ✅

---

# ⚠️ Why This Works

Because one side is guaranteed sorted.

That sorted side lets you decide safely.

---

# 💀 Common Mistakes

## Mistake 1

Using normal binary search blindly.

Fails because array not globally sorted.

---

## Mistake 2

Forgetting equality:

```python id="a8n6we"
nums[left] <= nums[mid]
```

Use `<=`, not `<`

---

## Mistake 3

Wrong target range checks.

Need:

```python id="n4v7rt"
nums[left] <= target < nums[mid]
```

---

# 🔴 Problem 81 - Search in Rotated Sorted Array II

Same as Problem 33 but duplicates exist.

Example:

```python id="r3p6lo"
[2,5,6,0,0,1,2]
```

Now difficult because:

```python id="x5m8qe"
nums[left] == nums[mid] == nums[right]
```

Cannot know sorted side.

---

# ✅ Trick

Shrink both sides:

```python id="j1s7wb"
left += 1
right -= 1
```

Then continue.

---

# Code

```python id="t8q4nd"
def search(nums, target):
    left, right = 0, len(nums)-1

    while left <= right:
        mid = (left + right)//2

        if nums[mid] == target:
            return True

        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1

        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return False
```

---

# 🧠 Interview Pattern Recognition

If question says:

* Sorted array rotated
* Search in circular sorted array
* Pivoted sorted array

Think:

> Rotated Binary Search

---

# 🏆 Outcome Today

After Day 3 you should be able to:

✅ Detect sorted half instantly
✅ Solve LeetCode 33
✅ Handle duplicates in 81
✅ Use binary search on modified arrays

---

# 🔥 Homework

Solve:

1. 33 Search in Rotated Sorted Array
2. 81 Search in Rotated Sorted Array II

Then explain aloud:

> Why one half is always sorted.

---