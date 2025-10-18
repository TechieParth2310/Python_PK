# 📚 Python Lists — Pro-Level Notes 

---

## 📘 Introduction

A **list** is Python’s go-to **mutable, ordered** sequence type that can hold **heterogeneous** objects:
```python
nums = [1, 2, 3]
mix  = [1, "chai", 3.14, True, [5, 6]]
```
- ✅ **Ordered** → preserves insertion order
- ✅ **Mutable** → elements can be changed in-place
- ✅ **Heterogeneous** → any types inside
- ✅ **Iterable** → loops, comprehensions
- ⚠️ **Not hashable** → cannot be dict keys or set elements

---

## 🔹 Creation & Basic Operations

```python
lst = []                      # empty
lst = list()                  # also empty
lst = [10, 20, 30]            # literal
lst = list("abc")             # ['a', 'b', 'c'] (from iterable)
lst = [0] * 5                 # [0, 0, 0, 0, 0] (repeat)
```

```python
len(lst)                      # size
lst[0], lst[-1]               # indexing (first, last)
lst[1:4], lst[:], lst[::-1]   # slicing (copy is lst[:])
3 in lst, 42 not in lst       # membership
```

---

## ✏️ Mutability (In-Place Edits)

```python
lst = [10, 20, 30]
lst[1] = 99                   # [10, 99, 30]
lst[0:2] = [1, 2, 3]          # [1, 2, 3, 30]  (slice assign can change length)
del lst[2]                    # delete by index
del lst[:]                    # clear all (same as lst.clear())
```

> 🧠 **Slice assignment** can insert/replace multiple elements at once and change list length.

---

## 🧰 Core Methods (with Gotchas)

| Method | What it does | Returns | Notes |
|---|---|---|---|
| `append(x)` | add at end | `None` | O(1) amortized |
| `extend(it)` | add all from iterable | `None` | don’t do `append(list)` if you want to flatten |
| `insert(i, x)` | insert at index | `None` | O(n) shift right |
| `pop([i])` | remove & return | element | default last; O(1) end, O(n) middle |
| `remove(x)` | remove first equal x | `None` | ValueError if not found; O(n) |
| `clear()` | remove all | `None` | |
| `index(x[, start, end])` | position of x | int | ValueError if missing |
| `count(x)` | occurrences | int | O(n) |
| `sort(*, key=None, reverse=False)` | in-place sort | `None` | Timsort; stable; O(n log n) |
| `reverse()` | in-place reverse | `None` | |
| `copy()` | shallow copy | list | same as `lst[:]` |

> ⚠️ Many list methods **return `None`** because they mutate in-place.  
> Don’t do: `lst = lst.sort()` (you’ll get `None`). Use `lst.sort()` or `sorted(lst)`.

---

## 🔄 Concatenation vs Extend

```python
a = [1, 2]; b = [3, 4]
c = a + b            # new list [1, 2, 3, 4]
a.extend(b)          # a becomes [1, 2, 3, 4] (mutates)
```

- `+` creates a **new** list (O(n+m))
- `extend` mutates the **left** list in place (O(m))

---

## 🧮 Sorting: Key Functions & Stability

```python
words = ["Tea", "chai", "Chai", "code"]
words.sort(key=str.lower)              # case-insensitive
words.sort(key=len, reverse=True)      # by length desc
sorted_nums = sorted({3, 1, 2})        # returns NEW list
```
- **Stable**: equal keys preserve original order (great for multi-key sorting: sort by secondary key first, then primary).

---

## 🧩 Copying Lists — Shallow vs Deep

```python
import copy
x = [[1, 2], [3, 4]]

shallow = x.copy()              # or x[:]
shallow[0][0] = 99              # affects x too (inner is shared)

deep = copy.deepcopy(x)
deep[0][0] = 111                # independent
```
- **Shallow**: new outer list; inner objects shared  
- **Deep**: recursively copies all levels

---

## 🧠 Dry Run — Shallow Copy Pitfall

| Step | Code | `x` | `shallow` |
|---|---|---|---|
| 1️⃣ | `x = [[1,2],[3,4]]` | `[[1,2],[3,4]]` | — |
| 2️⃣ | `shallow = x[:]` | same object | new outer list, same inner refs |
| 3️⃣ | `shallow[0][0] = 99` | `[[99,2],[3,4]]` | `[[99,2],[3,4]]` |

> 💥 Inner lists are shared; mutate them and both reflect the change.

---

## 🧱 List Comprehensions (Fast & Pythonic)

**Basic:**
```python
squares = [n*n for n in range(6)]          # [0, 1, 4, 9, 16, 25]
evens   = [n for n in range(10) if n % 2 == 0]
```

**Nested:**
```python
pairs = [(i, j) for i in range(2) for j in range(3)]
# [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2)]
```

**Transform + Filter:**
```python
cleaned = [s.strip().lower() for s in raw if s]   # drop falsy, normalize
```

> ⚡ Comprehensions are faster than `append` loops in CPython for many cases.  
> For **very large** pipelines, consider generator expressions to save memory:
```python
gen = (process(x) for x in huge_iterable)   # lazy, memory-efficient
```

---

## 🧭 Unpacking, Star, and Swaps

```python
a, b = [1, 2]                # unpack
a, b = b, a                  # swap without temp
head, *mid, tail = [1,2,3,4,5]  # head=1, mid=[2,3,4], tail=5
```

---

## 🔎 Enumerate & Zip (Loop Like a Pro)

```python
for i, val in enumerate(["a","b","c"], start=1):
    print(i, val)

for k, v in zip(["name","lang"], ["Hitesh","Python"]):
    print(k, "→", v)
```

---

## 🧱 Nested Lists & “Matrix”-Like Ops

```python
mat = [
  [1, 2, 3],
  [4, 5, 6],
]
col0 = [row[0] for row in mat]          # [1, 4]
transposed = list(zip(*mat))            # [(1,4),(2,5),(3,6)]
```

> For heavy numerical work, prefer **NumPy arrays**. Lists are general-purpose, not vectorized.

---

## 🧵 Performance & Big-O Cheatsheet

- Index access: **O(1)**
- Append (amortized): **O(1)**
- Pop at end: **O(1)**; pop/insert in middle: **O(n)**
- Membership `x in lst`: **O(n)**
- Sort: **O(n log n)**
- Extend by *m* items: **O(m)**

> 🔧 For frequent **left pops/appends**, use `collections.deque` (O(1) at both ends).

---

## 🧨 Common Pitfalls

1) **Default Mutable Arguments**
```python
def bad(acc=[]):            # ❌ same list reused across calls
    acc.append(1); return acc

def good(acc=None):         # ✅ create fresh when needed
    if acc is None: acc = []
    acc.append(1); return acc
```

2) **Multiplying Nested Lists**
```python
grid = [[0]*3]*3            # ❌ inner rows aliased
grid[0][0] = 1              # changes all first elements
# [[1,0,0],[1,0,0],[1,0,0]]

grid = [[0]*3 for _ in range(3)]   # ✅ distinct rows
```

3) **Confusing `sort()` vs `sorted()`**
- `lst.sort()` → in-place, returns `None`
- `sorted(lst)` → returns **new** list

---

## 💻 Code Example (End-to-End)

```python
# Build, mutate, copy, sort, and comprehend
data = [5, 2, 9, 1, 5]
data.append(7)                  # [5,2,9,1,5,7]
data.remove(5)                  # remove first 5 → [2,9,1,5,7]
tail = data.pop()               # tail=7, data=[2,9,1,5]
view = data[:]                  # shallow copy
view[0] = 99                    # data unaffected → [2,9,1,5], view=[99,9,1,5]
data.sort()                     # [1,2,5,9]
desc = sorted(data, reverse=True)  # [9,5,2,1]
evens = [x for x in range(10) if x % 2 == 0]
pairs = [(i, j) for i in range(2) for j in range(2)]
```

---

## 🧠 Dry Run / Step-by-Step Execution

| Step | Code | Result / State | Why |
|---|---|---|---|
| 1️⃣ | `data = [5,2,9,1,5]` | `[5,2,9,1,5]` | start |
| 2️⃣ | `data.append(7)` | `[5,2,9,1,5,7]` | push end |
| 3️⃣ | `data.remove(5)` | `[2,9,1,5,7]` | removes first 5 |
| 4️⃣ | `tail = data.pop()` | `tail=7`, list `[2,9,1,5]` | pop end |
| 5️⃣ | `view = data[:]` | new list | shallow copy |
| 6️⃣ | `view[0] = 99` | `view=[99,9,1,5]` | data not affected |
| 7️⃣ | `data.sort()` | `[1,2,5,9]` | in-place |
| 8️⃣ | `desc = sorted(data, reverse=True)` | `[9,5,2,1]` | new list |

---

## 💡 Key Takeaways

- 🧩 Lists are **mutable, ordered, heterogeneous** sequences.  
- ✏️ Prefer **comprehensions** for clean + fast transforms.  
- 🧬 **Shallow copy** shares inner objects; use `deepcopy` for nested structures.  
- ⚙️ `sort()` mutates; `sorted()` returns a new list; sorting is **stable**.  
- 🚀 For queues/stacks: `list.append/pop` (end) is O(1); for two-sided ops use **`deque`**.

---

## 🚀 Pro Tips

- When you only need to **iterate once**, consider **generators** to save memory:
  ```python
  total = sum(x*x for x in range(10_000_000))
  ```
- For **unique items** or frequent membership tests, convert to **`set`**.  
- Large numeric workloads? Use **NumPy**; lists aren’t vectorized.  
- When building large lists progressively, prefer `append/extend` over `+` in loops.

---

## 🧾 Summary

✅ Lists are the **workhorse** of Python collections: flexible, fast for end-operations, and rich with methods.  
✅ Master slicing, comprehensions, copying semantics, and sorting to write **clean, efficient** Python.  
✅ Watch out for **mutable defaults** and **aliased rows** when multiplying nested lists.

---
