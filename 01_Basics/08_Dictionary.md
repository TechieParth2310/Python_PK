# 🗂️ Python Dictionaries — Beginner Edition (Short, Friendly, With Examples)

> A **dictionary** stores data as **key → value** pairs.  
> Think of it like a mini “contact book” where a **key** is the name, and the **value** is the number.

---

## ✅ What is a Dictionary?
```python
student = {"name": "Hitesh", "age": 20, "skills": ["python", "js"]}
# keys:   "name"   "age"     "skills"
# values: "Hitesh"   20      ["python","js"]
```
- **Ordered** (keeps the insert order)
- **Editable** (you can change it)
- **Fast lookups** by key

---

## ✨ Create a Dictionary
```python
empty = {}                                   # empty dict
user  = {"name": "Avi", "city": "Pune"}      # literal
pairs = dict([("a", 1), ("b", 2)])           # from list of pairs
```

---

## 🔎 Read (Access) Values
```python
user = {"name": "Avi", "city": "Pune"}

print(user["name"])        # Avi   (❗ KeyError if missing)
print(user.get("email"))   # None  (safe)
print(user.get("email", "N/A"))  # N/A (safe with default)
```

---

## ➕ Add / ✏️ Update Values
```python
user["email"] = "avi@mail.com"   # add new key
user["city"]  = "Mumbai"         # update existing key

user.update({"age": 21, "city": "Delhi"})  # add/update many at once
```

---

## ❌ Remove Values
```python
user.pop("age", None)   # remove "age" (return value or default if missing)
del user["city"]        # delete key (KeyError if missing)
user.clear()            # empty the dict
```

---

## 🔁 Looping Over a Dict
```python
user = {"name": "Avi", "city": "Delhi", "age": 21}

for key in user:                 # keys
    print(key)

for key, value in user.items():  # key & value
    print(key, "→", value)
```

---

## 🧰 Handy Everyday Methods (just a few!)
```python
user.keys()      # dict_keys([...])   → all keys
user.values()    # dict_values([...]) → all values
user.items()     # dict_items([...])  → (key, value) pairs

# Make a list once if you need to change while looping:
for k in list(user.keys()):
    if k == "age":
        del user[k]
```

---

## 🤝 Merge Two Dictionaries (Python 3.9+)
```python
a = {"x": 1, "y": 2}
b = {"y": 99, "z": 3}

c = a | b    # new dict → {'x':1, 'y':99, 'z':3}
a |= b       # in-place → a is now {'x':1, 'y':99, 'z':3}
```

---

## 🧪 Small Real Example (Beginner-Friendly)
```python
cart = {}
cart["apple"] = 2           # add
cart["banana"] = 5
cart["apple"] = 3           # update (now 3)

print(cart.get("orange", 0))  # 0 → not present, safe default

total_items = 0
for _, qty in cart.items():
    total_items += qty

print(cart)         # {'apple': 3, 'banana': 5}
print(total_items)  # 8
```

---

## ⚠️ Common Mistakes (and fixes)
1) **Using a list as a key** (lists change → not allowed)
```python
bad = {}
# bad[[1,2]] = "no"     # ❌ TypeError
good = {(1, 2): "ok"}    # ✅ use tuple (doesn’t change)
```

2) **Expecting a missing key to work**
```python
# user["email"]  # ❌ KeyError if email not there
user.get("email", "not given")  # ✅ safe
```

3) **Changing the dict while looping it directly**
```python
# for k in user: del user[k]   # ❌ RuntimeError
for k in list(user): del user[k]  # ✅ make a list copy of keys first
```

---

## 🧠 Tiny “Dry Run” (Step by Step)
```python
d = {"name": "Avi"}      # {'name': 'Avi'}
d["age"] = 21            # {'name': 'Avi', 'age': 21}
d.update(city="Pune")    # {'name': 'Avi', 'age': 21, 'city': 'Pune'}
d.pop("age", None)       # {'name': 'Avi', 'city': 'Pune'}
print(d.get("email", "N/A"))  # 'N/A'
```

---

## 🧾 TL;DR
- Use `d[key]` to access (fails if missing), or `d.get(key, default)` to be safe.  
- Add/update with `d[key] = value` or `d.update({...})`.  
- Remove with `pop`, `del`, or `clear`.  
- Loop with `for k, v in d.items(): ...`.  
- Keys must be **unchanging** (strings, numbers, tuples, etc.).

---
# 🔁 Looping Over Dictionaries — Quick, Practical Notes

---

## ✅ The 3 Common Ways

```python
d = {"name": "Avi", "age": 21, "city": "Pune"}

# 1) Keys (default)
for k in d:
    print(k, "→", d[k])

# 2) Keys explicitly
for k in d.keys():
    print(k)

# 3) Key + Value (most common)
for k, v in d.items():
    print(k, "→", v)

# Values only
for v in d.values():
    print(v)
```

**Tip:** Prefer `for k, v in d.items():` for clarity.  

---

## 🧭 Keep Order / Reverse / Index

```python
# Insertion order is preserved (Py 3.7+)
for k in d: ...
# Reverse order (Py 3.8+)
for k in reversed(d): ...
# With index (position in insertion order)
for i, (k, v) in enumerate(d.items(), start=1):
    print(i, k, v)
```

---

## 🧹 Modifying While Looping (Do it Safely)

❌ Don’t mutate the same dict you’re iterating:
```python
# for k in d: del d[k]   # RuntimeError
```

✅ Use a list of keys **or** build a new dict:
```python
# Delete some keys safely
for k in [k for k, v in d.items() if v is None]:
    del d[k]

# Transform into a new dict
new_d = {k: v*2 for k, v in d.items() if isinstance(v, int)}
```

---

## 🔠 Sorting During Iteration

```python
# Sort by key
for k in sorted(d):
    print(k, d[k])

# Sort by value
for k, v in sorted(d.items(), key=lambda kv: kv[1]):
    print(k, v)

# Sort by custom rule (length of key, desc)
for k, v in sorted(d.items(), key=lambda kv: len(kv[0]), reverse=True):
    print(k, v)
```

---

## 🧺 Grouping / Counting While Looping

```python
# Group items by first letter of key
from collections import defaultdict
group = defaultdict(list)
for k, v in d.items():
    group[k[0]].append((k, v))

# Count values quickly
from collections import Counter
cnt = Counter(d.values())
for val, freq in cnt.items():
    print(val, "→", freq)
```

---

## 🧩 Nested Dictionaries

```python
cfg = {
  "db": {"host": "localhost", "port": 5432},
  "auth": {"token": "xyz", "ttl": 3600},
}

for section, inner in cfg.items():
    for k, v in inner.items():
        print(f"[{section}] {k} = {v}")
```

---

## ⚡ Useful Patterns

```python
# Detect missing and initialize on the fly
for k, v in [("py", 1), ("js", 2), ("py", 3)]:
    d.setdefault(k, []).append(v)

# Consume a dict (pop as you go)
while d:
    k, v = d.popitem()   # LIFO
    print(k, v)
```

---

## 🧾 TL;DR
- Use `for k, v in d.items():` most of the time.  
- Don’t modify the dict you’re iterating — use `list(d)` or build a new dict via comprehension.  
- Sort with `sorted(d)` or `sorted(d.items(), key=...)` when you need order.  
- For nested dicts, loop `for outer, inner in d.items():` then `for k, v in inner.items():`.

---

# 🧮 Dictionary Comprehension — Smart Way to Build Dicts

---

## 📘 What is Dictionary Comprehension?

Just like list comprehensions, **dictionary comprehensions** let you **create dictionaries in one line** using a `for` loop.

📌 **Syntax:**
```python
{key_expression : value_expression for item in iterable if condition}
```

It’s short, fast, and **Pythonic** 🐍

---

## 💻 Example 1 — Basic Square Mapping

```python
squared_num = {x: x**2 for x in range(6)}
print(squared_num)
```

🧠 **Output:**
```
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

Here:
- Keys → numbers from 0 to 5  
- Values → their squares  

### ✅ Equivalent long form:
```python
squared_num = {}
for x in range(6):
    squared_num[x] = x**2
```

---

## 💻 Example 2 — With Condition (Filter)

```python
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)
```

🧠 **Output:**
```
{0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```
Only even numbers are included because of the `if` condition.

---

## 💻 Example 3 — Using Strings

```python
word = "chai"
ascii_map = {ch: ord(ch) for ch in word}
print(ascii_map)
```

🧠 **Output:**
```
{'c': 99, 'h': 104, 'a': 97, 'i': 105}
```

💡 The `ord()` function gives the ASCII number of a character.

---

## 💻 Example 4 — Swapping Keys and Values

```python
data = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in data.items()}
print(swapped)
```

🧠 **Output:**
```
{1: 'a', 2: 'b', 3: 'c'}
```

---

## 💻 Example 5 — Nested Comprehension (Advanced)

```python
matrix = {(i, j): i*j for i in range(1, 4) for j in range(1, 4)}
print(matrix)
```

🧠 **Output:**
```
{(1,1):1, (1,2):2, (1,3):3, (2,1):2, (2,2):4, (2,3):6, (3,1):3, (3,2):6, (3,3):9}
```

> Useful for generating lookup tables or coordinate data.

---

## 💻 Example 6 — Clear the Dict
```python
squared_num.clear()
print(squared_num)   # {}
```

---

## 🧠 Dry Run (for `{x:x**2 for x in range(4)}`)
| Step | x | Expression | Result so far |
|------|---|-------------|----------------|
| 1️⃣ | 0 | 0**2 → 0 | {0: 0} |
| 2️⃣ | 1 | 1**2 → 1 | {0: 0, 1: 1} |
| 3️⃣ | 2 | 2**2 → 4 | {0: 0, 1: 1, 2: 4} |
| 4️⃣ | 3 | 3**2 → 9 | {0: 0, 1: 1, 2: 4, 3: 9} |

---

## 💡 Key Takeaways

- 🧠 `{k:v for ...}` → quick & clean way to build dictionaries  
- ⚙️ Works with conditions and multiple loops  
- 🧾 Same result as normal for-loop but **shorter & faster**  
- 🔄 Use `clear()` to empty a dictionary anytime  
- 💬 Common use cases → mapping, filtering, swapping, quick lookups  

---

## 🚀 Pro Tip

You can combine dictionary comprehension with functions:
```python
def cube(n): return n**3
cube_dict = {x: cube(x) for x in range(1,6)}
print(cube_dict)  # {1:1, 2:8, 3:27, 4:64, 5:125}
```

Short, clean, and efficient 🔥

---
