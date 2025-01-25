from collections import deque

N, M = map(int, input().split())

routes = [[] for i in range(N)]
for j in range(M):
    a, b = map(int, input().split())
    routes[a-1].append(b-1)
    routes[b-1].append(a-1)
    
inf = 10**10

dist = [inf]*N
visited = [False] * N

now = 0
dist[now] = 0
visited[now] = True

que = deque()
que.append(now)

while que:
    now = que.popleft()
    for k in routes[now]:
        if visited[k] == False:
            visited[k] = True
            dist[k] = dist[now] + 1
            que.append(k)
            
for l in dist:
    if l != inf:
        print(l)
    else:
        print(-1)

