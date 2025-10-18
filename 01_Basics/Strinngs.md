# 🧵 Strings in Python — Complete Notes

---

## 📘 Introduction

Strings are one of Python’s most commonly used **sequence data types**.  
A **string** is simply a **collection of characters enclosed in quotes** — single `' '`, double `" "`, or triple quotes `''' '''` / `""" """`.

Strings in Python are:
- **Immutable** → can’t be changed after creation.
- **Ordered** → indexing and slicing are allowed.
- **Iterable** → can be looped character by character.

---

## 🔹 String Creation

```python
str1 = 'hello'
str2 = "chai aur code"
str3 = '''Python is awesome'''
```

✅ You can use single, double, or triple quotes.  
Triple quotes are often used for **multi-line strings**.

---

## 🔹 Accessing Characters

Strings behave like arrays — you can access characters using indexes (starting from `0`).

```python
name = "python"
print(name[0])  # p
print(name[5])  # n
```

📌 Negative indexing is also allowed:
```python
print(name[-1])  # n (last character)
print(name[-3])  # h
```

---

## 🔹 String Slicing

Slicing extracts parts of a string:
```python
text = "Python"
print(text[0:4])   # Pyth
print(text[:3])    # Pyt
print(text[2:])    # thon
print(text[-3:])   # hon
```

✅ Syntax → `string[start:end:step]`
- Start → inclusive
- End → exclusive
- Step → optional (defaults to 1)

### Example:
```python
word = "chai"
print(word[::-1])  # iahc (reverse)
```

---

## 🔹 String Immutability

Once a string is created, it **cannot be changed**.  
You can only **reassign** a new value.

```python
greet = "hello"
# greet[0] = 'H' ❌ TypeError
greet = "Hello"   # ✅ New string assigned
```

---

## 🔹 String Concatenation and Repetition

```python
s1 = "chai"
s2 = "code"
print(s1 + s2)     # chaicode
print(s1 * 3)      # chaichaichai
```

💡 Use `+` for joining and `*` for repetition.

---

## 🔹 Membership Operators

```python
name = "chai aur code"
print("chai" in name)     # True
print("python" not in name)  # True
```

✅ `in` checks for substring existence.

---

## 🔹 String Functions & Methods

| Method | Description | Example |
|--------|--------------|----------|
| `len()` | Returns string length | `len("chai") → 4` |
| `upper()` | Converts to uppercase | `"chai".upper() → 'CHAI'` |
| `lower()` | Converts to lowercase | `"CODE".lower() → 'code'` |
| `title()` | Capitalizes first letter of each word | `"chai aur code".title()` |
| `capitalize()` | Capitalizes only first letter | `"hello world".capitalize()` |
| `count(sub)` | Counts occurrences of substring | `"chai".count('a') → 1` |
| `find(sub)` | Finds first index of substring | `"chai".find('i') → 3` |
| `replace(a,b)` | Replace substring | `"chai".replace('chai','tea')` |
| `strip()` | Removes whitespace | `" hello ".strip() → 'hello'` |
| `split()` | Splits into list | `"chai aur code".split() → ['chai','aur','code']` |
| `join()` | Joins list into string | `" ".join(['chai','aur','code']) → 'chai aur code'` |
| `startswith()` | Checks start substring | `"chai".startswith('ch') → True` |
| `endswith()` | Checks end substring | `"chai".endswith('i') → True` |

---

## 💻 Code Example

```python
text = "   chai aur code  "

print(len(text))           # 17
print(text.strip())        # 'chai aur code'
print(text.upper())        # '   CHAI AUR CODE  '
print(text.replace("chai", "tea"))  # '   tea aur code  '

sentence = "python is fun"
print(sentence.split())    # ['python', 'is', 'fun']
print("-".join(["chai", "aur", "code"]))  # 'chai-aur-code'
```

---

## 🔹 String Formatting

Python supports multiple ways to format strings dynamically.

### 1️⃣ Using f-strings (modern and preferred)
```python
name = "Hitesh"
lang = "Python"
print(f"Hello {name}, welcome to {lang}!")
```

Output →  
`Hello Hitesh, welcome to Python!`

### 2️⃣ Using `format()`
```python
print("Hello {}, welcome to {}".format(name, lang))
```

### 3️⃣ Using `%` formatting
```python
print("Hello %s, you got %d points" % ("Hitesh", 95))
```

---

## 🔹 Escape Sequences

Used to insert special characters inside strings.

| Escape | Meaning | Example |
|---------|----------|----------|
| `\'` | Single quote | `'It\'s Python'` |
| `\"` | Double quote | `"He said \"Hello\""` |
| `\\` | Backslash | `'C:\\new\\folder'` |
| `\n` | New line | `'Hello\nWorld'` |
| `\t` | Tab space | `'Hello\tWorld'` |

---

## 🔹 Raw Strings

Prefix `r` to ignore escape sequences.

```python
path = r"C:\new\folder"
print(path)  # C:\new\folder
```

---

## 🔹 Multi-line Strings

Triple quotes (`'''` or `"""`) are used for multi-line strings.

```python
msg = """This is
a multi-line
string example."""
print(msg)
```

---

## 🔹 Iterating Over a String

```python
for ch in "chai":
    print(ch)
```

🧠 Strings are iterable — each loop iteration returns one character.

---

## 🔹 Comparing Strings

Strings can be compared lexicographically (alphabetical order).

```python
print("apple" < "banana")  # True
print("chai" == "chai")    # True
print("code" > "chai")     # True
```

🔤 Comparison is case-sensitive — uppercase letters come before lowercase in ASCII.

---

## 🧠 Dry Run / Step-by-Step Execution

| Step | Code | Output | Explanation |
|------|------|---------|-------------|
| 1️⃣ | `"chai"[0]` | `'c'` | Access first char |
| 2️⃣ | `"chai"[-1]` | `'i'` | Access last char |
| 3️⃣ | `"chai aur code".split()` | `['chai','aur','code']` | Split into list |
| 4️⃣ | `" ".join(['chai','aur','code'])` | `'chai aur code'` | Join list |
| 5️⃣ | `len("chai")` | `4` | Length of string |
| 6️⃣ | `"code" * 3` | `'codecodecode'` | Repeat string |

---

## 💡 Key Takeaways

- Strings are **immutable sequences** of Unicode characters.  
- Use slicing and indexing to extract substrings.  
- Use `+`, `*`, `in`, and `not in` for manipulation.  
- Use built-in methods (`upper()`, `split()`, `join()`, etc.) for fast operations.  
- f-strings (`f" "`) are the **modern and fastest** way to format strings.  

---

## 🚀 Pro Tips

- Always use `strip()` when handling user input to remove extra spaces.  
- Use `r"..."` for file paths and regex to avoid escape character confusion.  
- When comparing strings case-insensitively, use:
  ```python
  s1.lower() == s2.lower()
  ```
- For multi-line text, prefer triple quotes (`'''` / `"""`).

---

## 🧾 Summary

✅ **Strings are sequences** → support indexing, slicing, iteration.  
✅ **Immutable** → once created, can’t be modified.  
✅ **Rich methods** → `split()`, `join()`, `replace()`, `strip()`, etc.  
✅ **Formatting** → f-strings, `.format()`, `%`  
✅ **Supports operations** → concatenation, repetition, comparison, membership.  

---

