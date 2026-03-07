# **Week 1 — Day 2: Array Patterns**

## **Goal**

* Understand **prefix sums and running sums**
* Learn to **avoid nested loops** using precomputed sums
* Practice **array manipulation problems**

---

## **Concepts to Cover**

### 1. **Prefix Sum**

* Precompute sums of elements up to each index
* Helps answer **sum queries efficiently**
* Example:

```python
nums = [1, 2, 3, 4]
prefix = [0] * (len(nums) + 1)

for i in range(len(nums)):
    prefix[i+1] = prefix[i] + nums[i]

# Sum of subarray nums[i:j] = prefix[j] - prefix[i]
print(prefix)  # [0, 1, 3, 6, 10]
```

### 2. **Running Sum**

* Keep updating a variable as you traverse
* Avoids recomputing sums repeatedly

```python
nums = [1, 2, 3, 4]
running_sum = []
total = 0
for num in nums:
    total += num
    running_sum.append(total)
print(running_sum)  # [1, 3, 6, 10]
```

### 3. **Product of Array Except Self**

* Use **prefix and suffix product arrays**
* Avoid division to handle zeros safely

```python
nums = [1,2,3,4]
n = len(nums)
left = [1]*n
right = [1]*n

for i in range(1,n):
    left[i] = left[i-1]*nums[i-1]

for i in range(n-2,-1,-1):
    right[i] = right[i+1]*nums[i+1]

result = [left[i]*right[i] for i in range(n)]
print(result)  # [24,12,8,6]
```

---

## **Practice Problems (Day 2)**

| Problem                             | Difficulty | Focus                            |
| ----------------------------------- | ---------- | -------------------------------- |
| **Running Sum of 1D Array**         | Easy       | Simple prefix sum                |
| **Product of Array Except Self**    | Medium     | Prefix/suffix trick              |
| **Best Time to Buy and Sell Stock** | Easy       | Track min while traversing array |

---

## **Step-by-Step Example: Best Time to Buy and Sell Stock**

```python
prices = [7,1,5,3,6,4]
min_price = float('inf')
max_profit = 0

for price in prices:
    min_price = min(min_price, price)
    max_profit = max(max_profit, price - min_price)

print(max_profit)  # Output: 5
```

* **Pattern:** Keep track of **current min or max** to avoid nested loops

---

## **Tips for Day 2**

1. Draw the array and prefix array for **visual understanding**.
2. Dry run **product except self** example on paper to see left/right accumulation.
3. Focus on **space/time optimization patterns**.

---

## **Daily Goal**

* Solve **all 3 practice problems**
* Note down **prefix/running sum patterns** in your notebook
* Make **1 diagram showing prefix and suffix products**

