from collections import Counter
arr = list(map(int,input().split()))
freq = Counter(arr)

ans = sum(num for num, count in freq.items() if count == 1)


print(ans)

