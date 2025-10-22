# sum of cube of numbers 

# given = list(map(int,input().split()))
# sum = 0 
# for num in range(given[0],given[1]+1):
#     sum = sum + num**3
    
# print(sum)

# Way 2 :- 

start,end = map(int,input().split())
cube_sum = sum(i**3 for i in range(start,end+1))
print(cube_sum)