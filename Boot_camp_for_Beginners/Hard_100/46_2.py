X = input()

l = len(X)

from collections import deque

q = deque()

ans = 0

for i in range(l):
    if X[i] == 'T':
        if len(q) == 0:
            ans += 1
        else:
            q.pop()
    else:
        q.append('S')

ans += len(q)

print(ans)