# 🐍 Internal Working of Python — Copy, Reference Counts & Slice

---

## 📘 Notes / Explanation

Python doesn’t store data *inside* variables like C or Java — instead, variables are **references** (or “labels”) to objects in memory 📦.  
Think of a variable as a **tag on a box** — multiple tags can point to the same box!

When we assign one variable to another, we don’t copy data; we just copy the reference.

---

## 🔹 Variable Assignment and Object References

When you do:
```python
x = [1, 2, 3]
y = x
```
➡️ Both `x` and `y` now point to the **same list** in memory.

So if one changes, both reflect it:
```python
y.append(4)
print(x)   # [1, 2, 3, 4]
```

Both variables are linked to the same object 🧩

---

## 🔹 Reference Counting

Python internally keeps a **reference count** for every object.  
When the count becomes zero → the object is automatically deleted by the **Garbage Collector (GC)** 🧹

Example:
```python
import sys

a = [10, 20, 30]
b = a
c = a

print(sys.getrefcount(a))  # usually prints 4
```
Explanation:
- `a`, `b`, and `c` refer to the same object.  
- `getrefcount()` adds one temporary reference while calling.

When all names go out of scope, the object is destroyed automatically ✅

---

## 🔹 Copying Objects (Shallow vs Deep)

Python’s `copy` module provides two ways to make copies:

### 📋 Shallow Copy  
Copies only the *outer* object; inner objects remain shared.

```python
import copy

x = [[1, 2], [3, 4]]
y = copy.copy(x)

y[0][0] = 99
print(x)   # [[99, 2], [3, 4]]
print(y)   # [[99, 2], [3, 4]]
```
👉 The inner list `[1, 2]` is shared — both got updated.

---

### 🧱 Deep Copy  
Creates a **completely independent copy**, including all nested elements.

```python
import copy

x = [[1, 2], [3, 4]]
y = copy.deepcopy(x)

y[0][0] = 99
print(x)   # [[1, 2], [3, 4]]
print(y)   # [[99, 2], [3, 4]]
```
✅ Changes in `y` don’t affect `x`.

---

## 🔹 Slicing — Hidden Copy Behavior

When you use slicing, e.g.:
```python
x = [10, 20, 30, 40]
y = x[:]
```
➡️ It creates a **new list**, but it’s still a **shallow copy**.  
Only the outer list is copied, not the inner contents.

```python
x = [[1, 2], [3, 4]]
y = x[:]

y[0][0] = 99
print(x)   # [[99, 2], [3, 4]]
```
The inner lists are still shared references 🔁

---

## 💻 Code Example
```python
import copy
import sys

print("---- Reference Count Example ----")
a = [1, 2, 3]
b = a
print("Reference count:", sys.getrefcount(a))  # usually 3 or 4

print("\n---- Shallow Copy Example ----")
x = [[10, 20], [30, 40]]
y = copy.copy(x)
y[0][0] = 999
print("x:", x)
print("y:", y)

print("\n---- Deep Copy Example ----")
z = copy.deepcopy(x)
z[0][0] = 111
print("x:", x)
print("z:", z)

print("\n---- Slice Copy Example ----")
nums = [5, 10, 15, 20]
copy_nums = nums[:]
print(nums is copy_nums)  # False (different lists)
print(nums == copy_nums)  # True (same values)
```

---

## 🧠 Dry Run / Step-by-Step Execution

| Step | Code | Explanation |
|------|------|--------------|
| 1️⃣ | `a = [1, 2, 3]` | Creates a new list in memory |
| 2️⃣ | `b = a` | `b` points to the same object as `a` |
| 3️⃣ | `copy.copy(x)` | Creates a new outer list, but inner lists are shared |
| 4️⃣ | `copy.deepcopy(x)` | Creates a new list and new inner lists |
| 5️⃣ | `x[:]` | Creates a shallow copy using slicing |

---

## 💡 Key Takeaways

- 🧩 **Assignment (`=`)** only links names — it doesn’t copy data.  
- 🪞 **Shallow Copy** → new outer container, shared inner elements.  
- 🧬 **Deep Copy** → full independent copy.  
- 🔁 **Slicing (`[:]`)** → shallow copy shortcut.  
- 🧹 **Reference Counting** → automatic memory cleanup when count = 0.

---

## 🚀 Pro Tips

- Use `id(object)` to check if two variables share the same memory reference.
- Avoid unnecessary deep copies in performance-critical code — they are expensive.
- Immutable types (`int`, `str`, `tuple`) behave differently — they’re copied by value automatically.

---

