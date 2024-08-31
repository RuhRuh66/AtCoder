N, M = map(int, input().split())

roads = [[] for i in range(N)]
for j in range(M):
    a, b= map(int, input().split())
    a, b = a-1, b-1
    roads[a].append(b)
    
from collections import deque

ans = 0
for k in range(N):
    q = deque()
    visited = [False] * N
    visited[k] = True
    q.append(k)
    while q:
        now = q.popleft()
        for n in roads[now]:
            if visited[n] == True:
                continue
            else:
                visited[n] = True
                q.append(n)
    ans += visited.count(True)

print(ans)
    