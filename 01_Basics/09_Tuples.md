# 🎯 Tuples in Python — Complete & Easy Notes

---

## 📘 Introduction

A **tuple** is just like a list, but it’s **immutable** (you can’t change it).  
It stores **ordered** and **indexed** items — just in a safer (unchangeable) way.

📌 You can think of a tuple as a **read-only list**.

---

## 🔹 Creating Tuples

```python
# Different ways to create a tuple
t1 = (1, 2, 3)
t2 = ("chai", "code", 42)
t3 = (10,)              # single element tuple (note the comma!)
t4 = tuple([1, 2, 3])   # using tuple() constructor
empty = ()              # empty tuple
```

⚠️ Don’t forget the comma for one-element tuples → `(10,)`  
Without it, Python treats it as just an integer.

---

## 🔹 Tuple Characteristics

- ✅ **Ordered** → items have fixed positions  
- ✅ **Immutable** → you can’t change, add, or delete elements  
- ✅ **Allows duplicates**  
- ✅ **Can hold mixed data types**

```python
data = (1, "chai", True, 3.14)
print(data)
```

---

## 🔹 Accessing Tuple Elements

Just like lists → use **indexing** and **slicing** 🎯

```python
nums = (10, 20, 30, 40, 50)

print(nums[0])    # 10
print(nums[-1])   # 50
print(nums[1:4])  # (20, 30, 40)
print(nums[::-1]) # (50, 40, 30, 20, 10)
```

---

## 🔹 Iterating Through a Tuple

```python
colors = ("red", "green", "blue")

for color in colors:
    print(color)
```

---

## 🔹 Tuple Methods (only two!)

| Method | Description | Example |
|--------|--------------|----------|
| `count(x)` | Counts how many times x appears | `(1,2,2,3).count(2) → 2` |
| `index(x)` | Returns first index of x | `(10,20,30).index(20) → 1` |

---

## 🔹 Tuple Packing & Unpacking

```python
# Packing
person = ("Avi", 21, "Pune")

# Unpacking
name, age, city = person
print(name)  # Avi
print(age)   # 21
print(city)  # Pune
```

💡 You can also use `*` to capture extra items:
```python
data = (1, 2, 3, 4, 5)
a, *b, c = data
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5
```

---

## 🔹 Tuples with Loops and Enumerate

```python
langs = ("python", "java", "c++")
for i, val in enumerate(langs):
    print(i, "→", val)
```

---

## 🔹 Nesting Tuples

You can put tuples inside tuples (multi-level data).

```python
nested = ((1, 2), (3, 4), (5, 6))
print(nested[1][0])  # 3
```

---

## 🔹 Tuple vs List (Quick Difference)

| Feature | List | Tuple |
|----------|------|--------|
| Mutability | ✅ Mutable | ❌ Immutable |
| Syntax | `[ ]` | `( )` |
| Methods | Many | Few (`count`, `index`) |
| Performance | Slower | Faster (immutable → hashable) |
| Use Case | When data changes | Fixed data / constants |

---

## 🔹 Why Use Tuples?

✅ Protect data from accidental modification  
✅ Faster than lists  
✅ Can be used as dictionary **keys** or inside **sets** (because immutable)  
✅ Save memory  

---

## 🔹 Tuple as Dict Key Example

```python
location = {}
location[(19.07, 72.87)] = "Mumbai"
location[(28.61, 77.20)] = "Delhi"

print(location)
# {(19.07, 72.87): 'Mumbai', (28.61, 77.20): 'Delhi'}
```

---

## 🔹 Conversion Between Tuple & List

```python
nums = [1, 2, 3]
t = tuple(nums)      # → (1, 2, 3)
nums2 = list(t)      # → [1, 2, 3]
```

---

## 🔹 Tuple Comprehension? (Not Exactly)

Tuples don’t support comprehensions directly — but you can make one using a generator:

```python
t = tuple(x**2 for x in range(5))
print(t)   # (0, 1, 4, 9, 16)
```

---

## 🧠 Dry Run Example

| Step | Code | Result | Explanation |
|------|------|---------|--------------|
| 1️⃣ | `t = (10,20,30,40)` | `(10,20,30,40)` | create tuple |
| 2️⃣ | `t[1]` | `20` | indexing |
| 3️⃣ | `t[1:3]` | `(20,30)` | slicing |
| 4️⃣ | `len(t)` | `4` | count elements |
| 5️⃣ | `t.count(20)` | `1` | number of occurrences |
| 6️⃣ | `t.index(30)` | `2` | position of 30 |

---

## 💡 Key Takeaways

- 🧱 Tuples are **immutable lists** — fixed, ordered, indexed.  
- 📦 Pack/unpack makes variable assignment easy.  
- ⚡ Faster & lighter than lists.  
- 🧩 Great for **returning multiple values** from a function.  
- 🔐 Use tuples when you want **read-only data**.

---

## 💻 Quick Mini Example

```python
# Returning multiple values from a function
def get_user():
    return ("Hitesh", 28, "India")

name, age, country = get_user()
print(f"{name} is {age} years old from {country}.")
```

🧠 **Output:**
```
Hitesh is 28 years old from India.
```

---

## 🧾 TL;DR
- Tuple = **immutable, ordered collection**.  
- Use `( )` instead of `[ ]`.  
- Only 2 methods → `count()` & `index()`.  
- Can unpack, nest, or use as dict keys.  
- Best for **fixed data** that shouldn’t change.
