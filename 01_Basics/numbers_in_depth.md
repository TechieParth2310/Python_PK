# 🔢 Numbers in Depth — Basic Operations and Type Conversions

---

## 📘 Notes / Explanation

In Python, numbers are first-class objects.  
We can perform arithmetic operations directly on variables or literals.  
Let’s explore the most common **numeric operations** and **type conversions** in Python.

---

## 💻 Basic Arithmetic Operations

```python
x = 2
y = 3
z = 4

x + y        # Addition → 5
40 + 2.23    # Addition between int and float → 42.23
```

🧠 Python automatically promotes smaller types (like `int`) to larger types (like `float`) during mixed operations — this is called **type promotion**.

---

## 🧩 String and Number Mixing (TypeError)

If you try to combine a string and a number directly, Python throws an error ⚠️

```python
'hitesh' + 3
# ❌ TypeError: can only concatenate str (not "int") to str
```

✅ To fix this, explicitly **convert the number** to a string or vice-versa.

```python
'hitesh' + str(3)     # 'hitesh3'
int(2.23)             # 2 (fraction part removed)
float(40)             # 40.0
```

---

## 🔡 String Concatenation

You can join strings directly using `+`:
```python
'chai' + 'code'   # 'chaicode'
```
✅ Both operands must be strings.  
Concatenation simply merges the text — it doesn’t insert spaces automatically.

---

## ⚙️ Multiple Assignments and Expressions

Python allows assigning and evaluating multiple variables in one line.

```python
x, y, z = 2, 3, 4
(x + 1, y * 2)     # (3, 6)
```

💡 This returns a **tuple** with both computed values.

---

## 🧮 Modulus, Power & Big Integers

### 🔹 Modulus `%`
Gives the remainder after division.

```python
y % 2   # 1
```

### 🔹 Exponentiation `**`
Raises one number to the power of another.

```python
z ** 2    # 16
z ** 5    # 1024
100 ** 2  # 10000
```

💡 Python supports **arbitrary precision integers**, so it can handle extremely large powers easily!

```python
2 ** 100
# 1267650600228229401496703205376
```

No overflow errors here — Python automatically manages big integer storage 🔥

---

## 🧠 Dry Run / Step-by-Step Execution

| Step | Code | Output | Explanation |
|------|------|---------|--------------|
| 1️⃣ | `x = 2; y = 3; z = 4` | — | Variable initialization |
| 2️⃣ | `x + y` | 5 | Basic addition |
| 3️⃣ | `40 + 2.23` | 42.23 | Automatic float promotion |
| 4️⃣ | `'hitesh' + 3` | ❌ Error | String + int not allowed |
| 5️⃣ | `int(2.23)` | 2 | Fraction part truncated |
| 6️⃣ | `float(40)` | 40.0 | Converts int to float |
| 7️⃣ | `'chai' + 'code'` | `'chaicode'` | String concatenation |
| 8️⃣ | `y % 2` | 1 | Remainder |
| 9️⃣ | `z ** 2` | 16 | Power |
| 🔟 | `2 ** 100` | Very large number | Python handles big ints easily |

---

## 💡 Key Takeaways

- ➕ You can freely mix numeric types; Python automatically promotes to float when needed.  
- 🔠 Strings can’t mix with numbers without explicit conversion.  
- 🧾 `int()` truncates decimals; `float()` converts integers to float.  
- ⚙️ `%` → Modulus (remainder), `**` → Power/exponentiation.  
- 🧮 Python integers have **unlimited precision** — no overflow errors!  

---

## 🚀 Pro Tips

- Use underscores for readability in large numbers:
  ```python
  big = 1_000_000_000   # same as 1000000000
  ```
- Use `divmod(a, b)` to get **(quotient, remainder)** together.
- Always convert explicitly between types (`str()`, `int()`, `float()`) when combining strings & numbers.

---
---

# 🧮 Numbers in Depth — Float Precision, `repr()`, `str()`, and `print()`

---

## 📘 Notes / Explanation

Let’s now look into **how Python represents numbers and strings internally** and how different display methods (`repr()`, `str()`, `print()`) behave.

---

## 🔹 Floating Point Division

```python
result = 1 / 3.0
result
```

🧠 Output:
```
0.3333333333333333
```

### 🔍 Explanation:
- Division of integers in Python 3 **always returns a float** (`/` operator).
- Floats can’t represent some decimals precisely because of **binary representation limits**.
- Python rounds to 17 significant digits by default when displaying floats.

✅ You can use:
```python
round(result, 2)  # → 0.33
```
to control precision during display.

---

## 🔹 The Difference Between `repr()`, `str()`, and `print()`

These three functions are used to **display or represent objects**, but each serves a different purpose:

| Function | Purpose | Example Output |
|-----------|----------|----------------|
| `repr()` | Developer representation (unambiguous) | `"'chai'"` |
| `str()` | User-friendly representation | `'chai'` |
| `print()` | Prints actual readable output | `chai` |

---

### 🧠 Example Breakdown

```python
repr('chai')   # → "'chai'"
str('chai')    # → 'chai'
print('chai')  # → chai
```

- **`repr()`**: Shows quotes → good for debugging or logging (tells you the data type is a string).
- **`str()`**: Returns a clean string format.
- **`print()`**: Displays the final readable form on the console.

---

## 🧠 Dry Run / Step-by-Step Execution

| Step | Code | Output | Explanation |
|------|------|---------|--------------|
| 1️⃣ | `result = 1 / 3.0` | 0.3333333333333333 | Float division result |
| 2️⃣ | `repr('chai')` | `"'chai'"` | Shows quotes — developer representation |
| 3️⃣ | `str('chai')` | `'chai'` | Shows value as plain string |
| 4️⃣ | `print('chai')` | `chai` | Prints user-readable form |

---

## 💡 Key Takeaways

- ⚙️ Python’s `/` always performs **float division** (even with integers).  
- 🧮 Floating-point arithmetic may produce long decimals due to binary limitations.  
- 🧾 `repr()` gives the **debug view**, `str()` gives the **user view**, and `print()` shows the **display view**.  
- ✅ Use `round()` or the `decimal` module for precise floating-point control.  

---

## 🚀 Pro Tip

- For debugging complex data types:
  ```python
  x = 'chai'
  print(repr(x))  # helpful for identifying spaces, escape chars, etc.
  ```
- When logging or serializing data, **prefer `repr()`** to capture exact object representation.

---

# 🔢 Numbers in Depth — Comparison Operators and Chained Conditions

---

## 📘 Notes / Explanation

Python allows rich **comparison operations** between numbers —  
you can directly check relationships like `<`, `>`, `==`, `!=`, etc.  
These comparisons always return a **Boolean value** (`True` or `False`) ✅

---

## 🔹 Basic Comparison Examples

```python
1 < 2        # True
5.0 == 5.0   # True
4.0 != 5.0   # True
```

### 🧠 Explanation:
- `1 < 2` → checks if 1 is less than 2 → ✅ `True`
- `5.0 == 5.0` → equality comparison → ✅ `True`
- `4.0 != 5.0` → checks inequality → ✅ `True`

💡 Python can compare integers and floats **seamlessly** —  
`5 == 5.0` is also `True` because both represent the same numeric value.

---

## 🔹 Multiple Comparisons in One Statement

Python supports **chained comparisons**, which make expressions clean and readable 👇

```python
x, y, z = 2, 3, 4
x < y < z
```

✅ Output: `True`

### ⚙️ Internally Equivalent To:
```python
x < y and y < z
```

But Python optimizes this automatically — it doesn’t evaluate the middle variable (`y`) twice ⚡  
That’s why `x < y < z` is both **efficient and Pythonic** 🐍

---

## 🧠 Dry Run / Step-by-Step Execution

| Step | Code | Result | Explanation |
|------|------|---------|--------------|
| 1️⃣ | `1 < 2` | True | 1 is less than 2 |
| 2️⃣ | `5.0 == 5.0` | True | Equal floats |
| 3️⃣ | `4.0 != 5.0` | True | Not equal |
| 4️⃣ | `x, y, z = 2, 3, 4` | — | Assigns values |
| 5️⃣ | `x < y < z` | True | Checks both conditions in one go |
| 6️⃣ | `x < y and y < z` | True | Equivalent expanded form |

---

## 💡 Key Takeaways

- ⚖️ Python supports all standard comparison operators:  
  `<`, `<=`, `>`, `>=`, `==`, `!=`
- 🧮 Integers and floats can be compared directly.
- 🔗 Chained comparisons (`x < y < z`) are cleaner and faster.
- 🧠 Logical operators like `and`, `or`, `not` can combine multiple comparisons.

---

## 🚀 Pro Tip

- Use chained comparisons for readability:
  ```python
  10 < score <= 100
  ```
  ✅ Checks if `score` is between 10 and 100 (inclusive).

- Avoid writing long nested comparisons using multiple `and` — chaining is **more Pythonic**.

---

# 🧮 Numbers in Depth — Floor and Truncate Methods (math module)

---

## 📘 Notes / Explanation

Python’s `math` module provides functions to handle **decimal rounding** and **integer conversion** precisely.  
Two commonly used ones are `math.floor()` and `math.trunc()`.  
They may seem similar — but they behave differently, especially with **negative numbers** ⚡

---

## 🔹 Importing the `math` Module

Before using math functions, always import it:
```python
import math
```

---

## 🔹 `math.floor(x)` — Round Down to Nearest Integer

```python
math.floor(3.5)   # 3
math.floor(-3.5)  # -4
math.floor(3.6)   # 3
math.floor(3.9)   # 3
```

### 🧠 Explanation:
- The **floor** function always rounds **toward negative infinity** (downward).  
- That’s why `math.floor(-3.5)` → `-4` (goes one step more negative).  

✅ **Rule:**  
> Always “round down” (even for negatives).

---

## 🔹 `math.trunc(x)` — Truncate Decimal Part

```python
math.trunc(2.8)    # 2
math.trunc(-2.8)   # -2
```

### 🧠 Explanation:
- `math.trunc()` **removes** the fractional part — it doesn’t round.  
- It just keeps the integer portion of the number, regardless of sign.

✅ **Rule:**  
> Simply chop off the decimal part (toward zero).

---

## ⚖️ Difference Between `floor()` and `trunc()`

| Function | 3.5 | -3.5 | Description |
|-----------|------|------|-------------|
| `math.floor()` | 3 | -4 | Rounds down toward -∞ |
| `math.trunc()` | 3 | -3 | Truncates toward 0 |

🧩 So, for positive numbers, both give same results.  
But for negative numbers → `floor()` goes more negative, while `trunc()` moves toward zero.

---

## 🧠 Dry Run / Step-by-Step Execution

| Step | Code | Output | Explanation |
|------|------|---------|--------------|
| 1️⃣ | `math.floor(3.5)` | 3 | Rounds down |
| 2️⃣ | `math.floor(-3.5)` | -4 | Goes toward -∞ |
| 3️⃣ | `math.trunc(2.8)` | 2 | Removes fraction part |
| 4️⃣ | `math.trunc(-2.8)` | -2 | Truncates toward zero |

---

## 💡 Key Takeaways

- 🔹 `math.floor()` → Always rounds **downward** (toward negative infinity).  
- 🔹 `math.trunc()` → Always **cuts off** decimals (toward zero).  
- 🧮 Useful for controlling numeric precision and integer logic in programs.

---

## 🚀 Pro Tips

- For **rounding to nearest integer**, use Python’s built-in `round()` instead of `math.floor()`.  
- Always `import math` before calling these functions.  
- For decimal precision instead of integers, use the `decimal` module.

---

# 🔢 Numbers in Depth — Number Systems and Base Conversions

---

## 📘 Notes / Explanation

Python supports **different number systems** like:
- 🟢 **Decimal** → Base 10 (normal numbers)
- 🟣 **Binary** → Base 2 (prefix `0b`)
- 🟠 **Octal** → Base 8 (prefix `0o`)
- 🔴 **Hexadecimal** → Base 16 (prefix `0x`)

These systems are super useful in **low-level programming, bitwise operations, and memory representation**.

---

## 🔹 Defining Numbers in Different Bases

```python
0o20      # Octal (base 8)
0xFF      # Hexadecimal (base 16)
0b1000    # Binary (base 2)
```

### 🧠 Output:
```
0o20   → 16
0xFF   → 255
0b1000 → 8
```

---

## 🔹 Invalid Octal Example

Octal digits can only be **0–7**.  
Using `8` or `9` throws an error ❌

```python
0o29
# SyntaxError: invalid digit '9' in octal literal
```

---

## 🔹 Converting Numbers Between Bases

Python provides built-in functions:
```python
oct(64)   # '0o100'
bin(64)   # '0b1000000'
hex(64)   # '0x40'
```

🧠 Converts decimal `64` into all three base representations.

---

## 🔹 Converting Strings to Integers with `int()`

You can also **interpret a string** as a number of a given base.

```python
int('64', 8)   # 52  → because '64' in octal = 52 in decimal
int('40', 16)  # 64  → because '40' in hex = 64 in decimal
```

💡 The second argument (`8`, `16`, etc.) tells Python what base the string uses.

---

## ⚠️ Common Error Example

If you try to use **invalid digits** for a base, Python raises a `ValueError`:
```python
int('1024', 2)
# ValueError: invalid literal for int() with base 2: '1024'
```

🔍 Why?  
Binary only allows digits `0` and `1`.  
The digit `2` or `4` makes it invalid for base 2.

---

## 🧠 Dry Run / Step-by-Step Execution

| Step | Code | Output | Explanation |
|------|------|---------|--------------|
| 1️⃣ | `0o20` | 16 | Octal → Decimal |
| 2️⃣ | `0xFF` | 255 | Hex → Decimal |
| 3️⃣ | `0b1000` | 8 | Binary → Decimal |
| 4️⃣ | `oct(64)` | `'0o100'` | Decimal → Octal string |
| 5️⃣ | `int('64', 8)` | 52 | Octal string → Decimal |
| 6️⃣ | `int('40', 16)` | 64 | Hex string → Decimal |
| 7️⃣ | `int('1024', 2)` | ❌ Error | Invalid binary digits |

---

## 💡 Key Takeaways

- 🔢 **Prefixes:**
  - Binary → `0b`
  - Octal → `0o`
  - Hexadecimal → `0x`
- ⚙️ **Conversion Functions:** `bin()`, `oct()`, `hex()`
- 📦 **String Conversion:** `int(<string>, <base>)`
- 🚫 Each base only allows specific digits:
  - Binary → 0,1  
  - Octal → 0–7  
  - Hex → 0–9, A–F (case-insensitive)

---

## 🚀 Pro Tips

- You can mix conversions easily:
  ```python
  hex(int('100', 2))  # Convert binary '100' → int → hex ('0x4')
  ```
- Great for debugging or reading memory addresses.  
- `bin()`, `oct()`, and `hex()` always return **strings**, not numbers.

---


