# 7. Function with *args
# Problem: Write a function that takes variable number of arguments and returns their sum.

def sum_all(*args):
    return sum(args)

print(sum_all(1,4,24,5))
