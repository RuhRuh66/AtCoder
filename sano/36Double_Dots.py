N, M = map(int, input().split())
routs = [[] for i in range(M)]
for i in range(M):
    A, B = map(int, input().split())
    A-=1
    B-=1
    routs[A].append(B)
    routs[B].append(A)
    
visited = [-1] * N
from collections import deque
s = deque()
