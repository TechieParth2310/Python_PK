# ✂️ List Slicing in Depth — Syntax, Patterns, Assignments, and Pitfalls

---

## 📘 What is Slicing?

Slicing returns a **new list** built from a **range of indices** of an existing list.

**General form:**  
`lst[start : stop : step]`

- `start` → first index to include (defaults to `0` for positive step, `len(lst)-1` for negative step)
- `stop`  → first index to **exclude** (defaults to `len(lst)` for positive step, `-1` sentinel for negative step)
- `step`  → stride (defaults to `1`). Can be **negative** to reverse direction.

> 🧠 Boundary-friendly: slices **never raise IndexError**; out-of-range indices are clamped.

---

## 🔹 Basics & Open-Ended Slices

```python
a = [10, 20, 30, 40, 50, 60]

a[1:4]    # [20, 30, 40]   (1..3)
a[:3]     # [10, 20, 30]   (start default)
a[3:]     # [40, 50, 60]   (stop default)
a[:]      # [10, 20, 30, 40, 50, 60]  (full shallow copy)
```

> ✅ `a[:]` is the standard **shallow copy** idiom for lists.

---

## 🔹 Stepped Slices (Every n-th Element)

```python
a[::2]    # [10, 30, 50]   (take every 2nd)
a[1::2]   # [20, 40, 60]   (odd positions if 0-based)
```

---

## 🔹 Negative Indices & Reverse Slicing

```python
a[-3:]      # [40, 50, 60]  (last three)
a[:-1]      # [10, 20, 30, 40, 50]  (exclude last)
a[::-1]     # [60, 50, 40, 30, 20, 10]  (reverse copy)
a[4:1:-1]   # [50, 40, 30]  (reverse window)
```

> 💡 `a[::-1]` is an **O(n)** reverse **copy**; use `a.reverse()` for in-place reverse.

---

## 🔹 Slice Assignment (Replace / Insert / Delete)

Slicing can also **modify** the list (because lists are mutable).

### 1) Replace a window
```python
a = [10, 20, 30, 40, 50]
a[1:4] = [99, 88]     # shorten window
# a → [10, 99, 88, 50]

a[2:2] = [7, 7, 7]    # insert at index 2 (empty window)
# a → [10, 99, 7, 7, 7, 88, 50]
```

### 2) Delete a window
```python
a = [1, 2, 3, 4, 5, 6]
del a[1:4]            # delete indices 1..3
# a → [1, 5, 6]

a[2:5] = []           # deletion via assignment
# same effect as del for that range
```

### 3) Assign to **extended slices** (with step)
> You can assign to `a[i:j:k]` **if** the replacement length equals the number of targeted positions.

```python
a = [0, 1, 2, 3, 4, 5, 6]
a[::2] = [100, 200, 300, 400]
# positions 0,2,4,6 replaced → a = [100, 1, 200, 3, 300, 5, 400]

# Length must match; otherwise ValueError:
# a[::2] = [1, 2]  → ValueError: attempt to assign sequence of size 2 to extended slice of size 4
```

### 4) Delete **extended slices**
```python
a = [0, 1, 2, 3, 4, 5, 6]
del a[::2]              # delete indices 0,2,4,6
# a → [1, 3, 5]
```

---

## 🔹 `slice()` Objects (Reusable Slices)

You can build a **slice object** and reuse it:

```python
win = slice(1, 5, 2)
a = [10, 20, 30, 40, 50, 60]
a[win]        # [20, 40]
```

Great for named/parameterized slicing in reusable utilities.

---

## 🔹 Out-of-Range Safety & Normalization

```python
a = [10, 20, 30]
a[-100:1000]   # [10, 20, 30]  (clamped, safe)
a[5:10]        # []            (empty, no error)
```

> 🧠 Slices **never** raise IndexError; plain indexing (e.g., `a[5]`) can.

---

## 🧪 Practical Patterns

### 1) Copy vs View
```python
b = a[:]       # shallow copy (new list, shared inner objects if nested)
```

### 2) Head, Tail, Middle
```python
head, tail = a[0], a[1:]
last, rest  = a[-1], a[:-1]
mid         = a[1:-1]
```

### 3) Chunking (fixed-size blocks)
```python
def chunks(seq, size):
    return [seq[i:i+size] for i in range(0, len(seq), size)]

chunks([1,2,3,4,5,6,7], 3)   # [[1,2,3],[4,5,6],[7]]
```

### 4) Even/Odd positions
```python
evens = a[::2]; odds = a[1::2]
```

### 5) Windowed reverse (palindrome checks)
```python
s = [1, 2, 3, 2, 1]
s == s[::-1]     # True
```

---

## 🧠 Dry Run / Step-by-Step

| Step | Code | Result | Why |
|---|---|---|---|
| 1️⃣ | `a = [10,20,30,40,50,60]` | — | setup |
| 2️⃣ | `a[1:4]` | `[20,30,40]` | 1..3 inclusive |
| 3️⃣ | `a[::-1]` | `[60,50,40,30,20,10]` | reversed copy |
| 4️⃣ | `a[::2]` | `[10,30,50]` | stride 2 |
| 5️⃣ | `a[1:1] = [99,99]` | `[10,99,99,20,30,40,50,60]` | insert |
| 6️⃣ | `del a[2:5]` | `[10,99,40,50,60]` | delete window |
| 7️⃣ | `a[::2] = [0,0,0]` | `[0,99,0,50,0]` | extended assign (len match) |

---

## ⚠️ Pitfalls & Performance

- **Extended slice assignment length must match** target count → or `ValueError`.
- `a[::-1]` creates a **new list**; prefer `a.reverse()` for in-place (no allocation).
- Chained slices like `a[::2][1:5]` create **intermediate copies**; combine into one slice when possible.
- Slicing is **O(k)** in length of the resulting slice; very large slices cost time/memory.

---

## 💻 Code Example (All-in-One)

```python
a = [10, 20, 30, 40, 50, 60]

# Basic windows
print(a[1:4], a[:3], a[3:], a[:])     # [20,30,40] [10,20,30] [40,50,60] full copy

# Steps & reverse
print(a[::2], a[1::2], a[::-1])       # [10,30,50] [20,40,60] reversed

# Insert / replace / delete
b = a[:]                  # shallow copy
b[2:4] = [99]             # replace window → [10,20,99,50,60]
b[3:3] = [7,7]            # insert at index 3 → [10,20,99,7,7,50,60]
del b[::2]                # delete even positions → [20,7,50]

# Extended assignment with equal-length replacement
c = [0,1,2,3,4,5,6,7]
c[::2] = [10,10,10,10]    # targets 0,2,4,6
print(c)                  # [10,1,10,3,10,5,10,7]
```

---

## 💡 Key Takeaways

- `lst[start:stop:step]` builds a **new list**; indices are clamped, safe from IndexError.  
- Negative `step` reverses direction; `a[::-1]` is a reverse **copy**.  
- Slice assignment lets you **insert/replace/delete** windows; extended assignment requires **length match**.  
- Prefer a **single slice** to avoid intermediate copies.  
- `a[:]` is the canonical **shallow copy** idiom.

---

## 🚀 Pro Tips

- For in-place reverse, use `lst.reverse()` (no extra memory).  
- For fast, memory-friendly pipelines, avoid chained slices; use iterators/generators when possible.  
- Parameterize slices with `slice(start, stop, step)` objects for reusable utilities.  
- When building 2D grids, beware of `[[0]*m]*n` aliasing—use comprehensions instead (see Lists pitfalls).

---
