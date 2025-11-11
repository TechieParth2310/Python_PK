# 🧩 Problem: Most Frequent Height Difference
# 📘 Given

# You’re given n tree heights → [h₁, h₂, h₃, ...]
# You must:

# Find absolute differences between adjacent trees.
# (Example: between h₁–h₂, h₂–h₃, etc.)

# Find which difference value occurs most frequently.

# Handle 2 edge cases:

# If any height is negative → print "invalid"

# If all differences are unique → print "non"


from collections import Counter

n = int(input())
heights = list(map(int, input().split()))

# Check for invalid case
if any(h < 0 for h in heights):
    print("invalid")
else:
    # Step 1: Find adjacent absolute differences
    diffs = [abs(heights[i] - heights[i+1]) for i in range(n-1)]
    
    # Step 2: Count frequency of each difference
    freq = Counter(diffs)
    
    # Step 3: Find most frequent difference
    most_common = freq.most_common(1)[0][1]  # get highest frequency
    
    if most_common == 1:
        print("non")
    else:
        # find the first difference that has this highest frequency
        print(freq.most_common(1)[0][0] ) 