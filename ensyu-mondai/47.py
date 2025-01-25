

N, M = map(int, input().split())
routes = [[] for i in range(N)]
for j in range(M):
    a, b = map(int, input().split())
    routes[a-1].append(b-1)
    routes[b-1].append(a-1)

visited = [0] * N

from collections import deque

s = deque()

for i in range(N):
    if visited[i] == 0:
        visited[i] = 1
        for t in routes[i]:
            if visited[t] == 0:
                visited[t] = -1
                s.append(t)
        
            elif visited[t] == -1:
                continue
            else:
                print('No')
                exit()
        while s:
            u = s.popleft()
            for v in routes[u]:
                if visited[v] == -visited[u]:
                    continue
                elif visited[v] == 0:
                    visited[v] = -visited[u]
                    s.append(v)
                else:
                    print('No')
                    exit()
print('Yes')