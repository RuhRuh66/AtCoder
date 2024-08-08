N = int(input())
A = [[] for _ in range(N)]
V = []

for i in range(N-1):
    a, b = map(int, input().split())
    A[a-1].append(b-1)
    A[b-1].append(a-1)
    V.append((a-1, b-1))
ma = 0

for i in range(N):
    temp = len(A[i])
    ma = max(ma, temp)
    
from collections import deque
q = deque()



