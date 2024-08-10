N = int(input())
from collections import deque

V = [[] for i in range(N)]

for i in range(N-1):
    u, v, w = map(int, input().split())
    V[u-1].append((u-1, v-1, w))
    V[v-1].append((v-1, u-1, w))
    
L = deque()

visited = [False] * N
colors = [-1] * N


visited[0] = True
colors[0] = 1
L.append(V[0])

while L:
    nex = L.popleft()
    for u, v, w in nex:
        if visited[v] == True:
            continue
        else:
            visited[v] = True
            L.append(V[v])
            if w % 2 == 1:
                colors[v] = 1 - colors[u]
            else:
                colors[v] = colors[u]
print(*colors)
                
    