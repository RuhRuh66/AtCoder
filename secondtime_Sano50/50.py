n, m, x, y = map(int, input().split())
x -= 1
y -= 1

graph = [[] for i in range(n)]
for j in range(m):
    a, b, t, k = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, t, k))
    graph[b].append((a, t, k))
    

from heapq import heappush, heappop
from math import ceil


dist = [-1] * n

q = [(0, x)]

while q:
    c, now_city = heappop(q)
    if dist[now_city] != -1:
        continue
    dist[now_city] = c
    
    for nx, t, k in graph[now_city]:
        if dist[nx] != -1:
            continue
        departure = (ceil(c/k))*k
        heappush(q, (departure+t, nx))
        
print(dist[y])