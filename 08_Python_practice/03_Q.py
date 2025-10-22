n = int(input())
sales = {}
total_revenue = 0 
for _ in range(n):
    item,qty,price = input().split()
    qty = int(qty)
    price = int(price)
    sale = qty*price
    sales[item] = sales.get(item,0)+sale
    total_revenue += sale
    top_item = max(sales,key = sales.get)
    average = total_revenue /n
print(f'Most Sold item :{top_item}')
print(f'Total Revenue :{total_revenue:.2f}')
print(f'Avg Revenue :{average:.2f}')