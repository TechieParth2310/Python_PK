# Majority Element

arr = list(map(int,input().split()))
n = len(arr)
freq = {}

for num in arr:
    if num in freq:
        freq[num] +=1
    else:
        freq[num] =1

found = False

for key in freq:
    if freq[key]> n//3:
        print(key,end=' ')
        found = True
if not found:
    print(' No Majority')
