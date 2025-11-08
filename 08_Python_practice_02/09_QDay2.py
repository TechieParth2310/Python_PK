# 🧩 Question 9 — Product–Sum Difference
# 📘 Problem Statement:

# A product has a numeric code N printed on it.
# When the scanner reads the value, it calculates the price using this rule:

# Price = |(Product of digits) – (Sum of digits)|

# That means:

# Multiply all digits of N → get product

# Add all digits of N → get sum

# Subtract them

# Take absolute value (so it’s always positive)


N = int(input())
product_N = 1
sum_N = 0

digit = str(N)
for d in digit:
    product_N = product_N*int(d)
    sum_N = sum_N+int(d)

ans = abs(product_N-sum_N)
print(ans)
