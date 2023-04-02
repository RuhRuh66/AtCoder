from collections import defaultdict

A = [k for k in range(10)]

s = defaultdict(int)
for i in A:
    s[i] += 1
    
print(s)