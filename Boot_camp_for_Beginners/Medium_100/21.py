N = int(input())
from collections import defaultdict
from math import comb

A = list(map(int, input().split()))



B = defaultdict(int)

for i in range(N):
    B[A[i]] += 1
    
total = 0
for i, j in B.items():
    total += comb(j, 2)
    
for k in range(N):
    ans = total - B[A[k]]+1
    print(ans)

