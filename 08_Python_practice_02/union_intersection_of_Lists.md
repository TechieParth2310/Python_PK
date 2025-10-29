# & Union 🟢 and Intersection 🔵 of Lists in Python  

## 🧠 HM Notes / Explanation  

In Python, **lists** are ordered collections — but sometimes we need to  
**combine** or **compare** them efficiently.  

That’s where **Union** and **Intersection** come in 👇  

### 🟢 Union → Combine & Remove Duplicates  
> Returns all **unique** elements present in *either* of the lists.  

Think of it as an **OR** operation — if an element exists in *list1* or *list2*,  
it will appear once in the result.  

### 🔵 Intersection → Find Common Elements  
> Returns all elements that are **common to both lists**.  

Think of it as an **AND** operation —  
if an element exists in *both* lists, only then it appears in the result.

---

## 💻 Code Example  

```python
# Two sample lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# ✅ Union
union_list = list(set(list1) | set(list2))
print("Union:", union_list)

# ✅ Intersection
intersection_list = list(set(list1) & set(list2))
print("Intersection:", intersection_list)
```

🖥️ **Output:**
```
Union: [1, 2, 3, 4, 5, 6, 7, 8]
Intersection: [4, 5]
```

---

## ⚙️ Dry Run / Step-by-Step Execution  

| Step | Action | list1 | list2 | Result |
|------|---------|--------|--------|--------|
| 1 | Convert to sets | {1, 2, 3, 4, 5} | {4, 5, 6, 7, 8} | — |
| 2 | Union (&#124;) → combine unique | — | — | {1, 2, 3, 4, 5, 6, 7, 8} |
| 3 | Intersection (&amp;) → common | — | — | {4, 5} |
| 4 | Convert back to list | — | — | `[1, 2, 3, 4, 5, 6, 7, 8]`, `[4, 5]` |

> 🧩 Operators used:  
> `|` → Union  
> `&` → Intersection

---

## 🧩 Alternate Methods  

### 1️⃣ Using `+` and `set()`  
```python
union_list = list(set(list1 + list2))
```

### 2️⃣ Using List Comprehension for Intersection  
```python
intersection_list = [x for x in list1 if x in list2]
```

### 3️⃣ Using Built-in `set` Methods  
```python
set(list1).union(list2)
set(list1).intersection(list2)
```

### 4️⃣ Manual Loop Method (for logic clarity)
```python
union = list1.copy()
for i in list2:
    if i not in union:
        union.append(i)

intersection = [i for i in list1 if i in list2]
```

---

## ⚡ Performance Insights  

- ✅ **Set-based** methods → fastest (O(n))  
- ❌ Manual loops → slower (O(n²))  
- ⚠️ Sets are **unordered**, so order may differ  
- 🔁 Convert back to list for ordered outputs  

---

## 🧭 Real-Life Analogy  

Imagine two contact lists 📱  
- One from your phone  
- One from your email  

📦 **Union** → everyone you know (all unique contacts)  
🤝 **Intersection** → people common in both  

---

## 🎯 Key Takeaways  

- `|` → Union (combine unique elements)  
- `&` → Intersection (common elements only)  
- `set()` automatically removes duplicates 🧹  
- Use list comprehensions when order matters 🧩  
- Convert back to list before returning results  

---

## 💎 Quick Recap  

| Operation | Symbol | Description | Example Result |
|------------|---------|-------------|----------------|
| Union | `|` | Combines all unique items | `[1, 2, 3, 4, 5, 6, 7, 8]` |
| Intersection | `&` | Keeps only common items | `[4, 5]` |

---

🚀 **Pro Tip:**  
If you need **sorted** output:
```python
sorted(list(set(list1) | set(list2)))
```

✨ **Union → everything once**  
✨ **Intersection → only what’s common**  
That’s Python’s power of simplicity 🐍⚡
