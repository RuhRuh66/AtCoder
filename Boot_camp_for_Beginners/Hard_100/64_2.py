def dfs(v, visited, connect):
    visited[v] = True
    for to in connect[v]:
        if visited[to] == False:
            dfs(to, visited, connect)
            
N, M = map(int, input().split())

T = []
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    T.append([a, b])

ans = 0
for i in range(M):
    visited = [False] * N
    connect = [[] for _ in range(N)]
    for j in range(M):
        if j != i:
            a, b = T[j]
            connect[a].append(b)
            connect[b].append(a)
    
    dfs(0, visited, connect)
    
    if not all(visited):
        ans += 1
        
print(ans)
            
    

    