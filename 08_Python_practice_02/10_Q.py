def monkeys_left_on_tree(n, k, j, m, p):
    if n <= 0 or k <= 0 or j <= 0 or m < 0 or p < 0:
        return "INVALID INPUT"
    monkeys_eating_bananas = m // k
    monkeys_eating_peanuts = p // j
    total_eating_monkeys = monkeys_eating_bananas + monkeys_eating_peanuts
    if total_eating_monkeys >= n:
        return "Number of Monkeys left on the Tree: 0"
    else:
        monkeys_left = n - total_eating_monkeys
        return f"Number of Monkeys left on the Tree: {monkeys_left}"

n = int(input())
k = int(input())
j = int(input())
m = int(input())
p = int(input())
print(monkeys_left_on_tree(n, k, j, m, p))
