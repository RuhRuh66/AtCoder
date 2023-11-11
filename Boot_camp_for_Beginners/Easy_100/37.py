N, K, Q = map(int, input().split())
from collections import defaultdict

A = defaultdict(int)

for i in range(Q):
    a = int(input())
    A[a] += 1
    
for i in range(1, N+1):
    temp = K-(Q-A[i])
    if temp > 0:
        print('Yes')
    else:
        print('No')
        

    
    