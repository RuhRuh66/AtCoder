N = int(input())
A = list(map(int, input().split())
         )
from collections import defaultdict

D = defaultdict(int)
for i in range(N):
    D[A[i]] += 1
    
K = len(D.keys())

if (N-K) % 2 == 1:
    ans = K-1
else:
    ans = K
print(ans)