# 📘 Problem Statement:

# A watchmaker compares a new watch he made to a standard watch showing correct time.

# You’re given:

# The initial correct time on the standard watch: h hours, m minutes.

# The current time shown by the new watch: h1 hours, m1 minutes.

# The number of hours passed (x) on the standard watch since the initial time.

# Your job:
# 👉 Calculate by how many minutes the new watch is lagging (positive) or early (negative)
# compared to the correct time.


h,m = map(int,input().split())
h1,m1 = map(int,input().split())
x = int(input())

correct_time = (h*60+x*60)+m
new_watch_time = (h1*60)+m1

time_diff = -(new_watch_time-correct_time)
print(time_diff)