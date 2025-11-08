# 📘 Problem Statement

# A company records the daily sales of its employees.
# You are given the total number of days, followed by the sales amount per day.

# You need to find:
# 1️⃣ The total sales
# 2️⃣ The average sales per day
# 3️⃣ The highest sale
# 4️⃣ The lowest sale

N = int(input())
sales_amt = list(map(int,input().split()))


Total_sales = sum(sales_amt)
Avg_sales = Total_sales/N
Highest_sale = max(sales_amt)
Lowest_sale = min(sales_amt)
print(f'Total: {Total_sales}')
print(f'Avearge: {Avg_sales}')
print(f'Highest: {Highest_sale}')
print(f'Lowest: {Lowest_sale}')