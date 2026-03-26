# 📅 DAY 6 — Pattern Mastery

## 🎯 Today’s Goal

By the end of today, you should:

* See a problem → instantly know the pattern
* Stop “thinking from scratch”
* Build a **mental pattern library**

---

# 🧠 Core Pattern Map (YOU MUST MEMORIZE)

| Problem Type       | Pattern      | Core Idea                       |
| ------------------ | ------------ | ------------------------------- |
| Two Sum            | HashMap      | store complement                |
| Stock Buy/Sell     | Min Tracking | track lowest price so far       |
| Max Subarray       | Kadane       | running sum + reset if negative |
| Contains Duplicate | HashSet      | check “already seen”            |

---

# 🧠 Step 1 — What Each Pattern REALLY Means

## 1. Two Sum → HashMap

Meaning:

> “I want to find a pair, so I store what I need”

Key thought:

* current → check complement

Mental trigger:

* “pair / target sum”

---

## 2. Stock Problem → Min Tracking

Meaning:

> “Best profit depends on lowest point before now”

Key thought:

* keep `min_price`
* compute profit at each step

Mental trigger:

* “buy low, sell high”

---

## 3. Maximum Subarray → Kadane

Meaning:

> “If my current path becomes bad (negative), I restart”

Key thought:

* running sum
* reset when sum < 0

Mental trigger:

* “continuous subarray max/min”

---

## 4. Contains Duplicate → HashSet

Meaning:

> “I only care if I’ve seen something before”

Key thought:

* store seen elements
* instant check O(1)

Mental trigger:

* “repeat / duplicate / already exists”

---

# 🧠 Step 2 — How Your Brain Should Work Now

When you see a problem, DO NOT jump to code.

Instead ask:

1. Is it about **pairs?**
   → HashMap

2. Is it about **max profit over time?**
   → Min tracking

3. Is it about **continuous subarray?**
   → Kadane

4. Is it about **repetition?**
   → HashSet

---

# 🧪 Step 3 — Notebook Task (IMPORTANT)

Write this exactly in your notebook:

---

## DSA Pattern Sheet (Week 1)

**Two Sum**

* Pattern: HashMap
* Idea: store complement
* Trigger: pair / target sum

**Stock Problem**

* Pattern: Min tracking
* Idea: track lowest price
* Trigger: buy/sell profit

**Maximum Subarray**

* Pattern: Kadane
* Idea: reset if sum < 0
* Trigger: continuous subarray

**Contains Duplicate**

* Pattern: HashSet
* Idea: check if seen before
* Trigger: repetition

---

# 🧪 Step 4 — Revision Drill (30–40 min)

Do this:

### Round 1 (No Code)

For each problem:

* Say pattern out loud
* Explain idea in 2–3 lines

---

### Round 2 (Mental Simulation)

Pick random input and:

* Run Kadane in your head
* Run HashMap logic mentally
* Track min price step by step

---

# ⚠️ Common Mistakes Today

❌ Learning new problems (don’t)
❌ Memorizing code (don’t)
❌ Skipping mental explanation (big mistake)

---

# 🧠 Final Shift (THIS IS IMPORTANT)

Before:

> “How do I solve this problem?”

After:

> “Which pattern is this problem using?”

That shift = real DSA progress.

---