N, K = map(int, input().split())
from collections import defaultdict

D = defaultdict(int)

for i in range(1, N+1):
    t = i % K
    D[t] += 1
    
ans = 0

ans += D[0] ** 3
if K % 2 == 0:
    ans += D[K//2] ** 3
print(ans)