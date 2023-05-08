Q = int(input())
from collections import deque
A = deque()

for i in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        A.appendleft(x)
    elif t == 2:
        A.append(x)
    else:
        print(A[x-1])