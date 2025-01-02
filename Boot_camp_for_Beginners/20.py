N, M = map(int, input().split())

from collections import defaultdict

prov = defaultdict(list)

cities = []

for i in range(M):
    p, y = map(int, input().split())
    prov[p].append((y, i+1))
for j in range(N):
    prov[j+1] = sorted(prov[j+1])
        


ans = [''] * (M+1)

for k in range(N):
    l = len(prov[k+1])
    for m in range(l):
        a, b = prov[k+1][m]
        ans[b] = str(k+1).zfill(6) + str(m+1).zfill(6)
        
print(*ans[1:])
