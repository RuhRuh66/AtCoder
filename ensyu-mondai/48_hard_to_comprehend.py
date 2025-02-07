K = int(input())

inf = 10**10

dist = [inf] * K

from collections import deque
q = deque()

dist[1] = 1

q.append(1)

while q:
    v = q.popleft()
    v2 = (v*10) % K
    if dist[v2] > dist[v]:
        dist[v2] = dist[v]
        q.append(v2)
        
    v2 = (v+1) % K
    if dist[v2] > dist[v]+1:
        dist[v2] = dist[v] +1
        q.append(v2)

print(dist[0])
