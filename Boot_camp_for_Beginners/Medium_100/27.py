N = int(input())
s = input()
t = input()


import re

overlap = 0
for i in range(N):
    u = t[:i+1] + '$'
    r = re.compile(u)
    if re.search(r, s):
        overlap = i+1
    else:
        continue
print(2*N-overlap)
