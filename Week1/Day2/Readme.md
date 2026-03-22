# 📅 DAY 2 — Min/Max + Stock Problem

## 🎯 Today’s Target

By the end of today, you should:

* Think **greedily**, not brute-force
* Track the **“best so far”** dynamically
* Solve **Best Time to Buy/Sell Stock** without loops inside loops

---

# 🧠 Step 1 — Concept: Track Minimum

**Problem:**
You have prices for each day:

```
prices = [7, 1, 5, 3, 6, 4]
```

Goal: **Buy once, sell once, maximize profit**

---

### Brute-force Thinking (❌)

* Check every pair `(buy_day, sell_day)`
* Profit = sell - buy
* Time complexity = O(n²)

🚫 Slow. Not FAANG-level thinking.

---

### Optimized Thinking (✅)

* Track **minimum price so far**
* Compute **profit if sold today**
* Update **maximum profit**

**Greedy mindset:**

> Don’t look back unnecessarily — just keep the best you’ve seen so far

---

# 🔥 Step 2 — Pattern: “Track Best So Far”

Variables:

```python
min_price = float('inf')
max_profit = 0
```

For each price in the array:

1. If price < min_price → update `min_price`
2. Else → calculate `profit = price - min_price`
3. If profit > max_profit → update `max_profit`

---

## ✅ Example Dry Run

```
prices = [7, 1, 5, 3, 6, 4]
```

| Day | Price | min_price | Profit if sell today | max_profit |
| --- | ----- | --------- | -------------------- | ---------- |
| 0   | 7     | 7         | 0                    | 0          |
| 1   | 1     | 1         | 0                    | 0          |
| 2   | 5     | 1         | 4                    | 4          |
| 3   | 3     | 1         | 2                    | 4          |
| 4   | 6     | 1         | 5                    | 5          |
| 5   | 4     | 1         | 3                    | 5          |

Answer = **5**

---

# 🧠 Step 3 — Pattern Recognition

Whenever you see:

* “Maximize/minimize while traversing”
* “Sell after buy”
* Only **one pass is needed**

🔥 Think **Greedy → Track best so far**

**Variables to remember:**

```python
min_price, max_profit
```

---

# 🧪 Step 4 — Your Tasks

1. **Solve once** using this pattern (don’t look at solution)
2. **Explain logic without code** in words:

* “I keep track of minimum price I have seen so far”
* “I check profit if I sell today”
* “I update max profit `if profit > max profit`”

3. **Test with different inputs**:

```
prices = [3, 2, 6, 1, 4] → Answer?
prices = [7, 6, 4, 3, 1] → Answer?
```

---

# ⚠️ Mistakes to Avoid

❌ Trying brute-force<br>
❌ Forgetting “sell must come after buy”<br>
❌ Not updating min_price dynamically<br>

---
