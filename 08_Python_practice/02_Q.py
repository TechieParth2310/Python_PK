h,m = map(int,input().split())
h1,m1 = map(int,input().split())
x = int(input())

expected_time = (h+x)*60+m
actual_time = (h1)*60+m1

diff = actual_time - expected_time
print(-diff)