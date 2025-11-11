# Count Frequency:-

S = input().strip().lower()
freq={}
for ch in S:
    if ch==' ':
        continue
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1


for i,v in sorted(freq.items()):
    print(i,v)
