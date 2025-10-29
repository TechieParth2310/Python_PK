# Majority Element
array = list(map(int, input().split()))
freq = {}
ans = -1
N = len(array)

for num in array:
    freq[num] = freq.get(num, 0) + 1   # fix 1

for value in freq:
    if freq[value] > N // 3:          
        ans = value                    
        break

print(ans)
