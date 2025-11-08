#🔹 Q23 — Count Palindromic Substrings

S = input()
n = len(S)
count = 0
for i in range(n):
    for j in range(i,n):
        substr = S[i:j+1]
        if(substr==substr[::-1]):
            print(substr)
            count +=1
print(count)

