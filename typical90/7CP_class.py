N = int(input())
edges = [[] for i in range(N)]
for j in range(N-1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    edges[A].append(B)
    edges[B].append(A)


dist = [0] * N

def dfs(x, last=-1):
    global dist
    for to in edges[x]:
        if to == last:
            continue
        dist[to] = dist[x] + 1
        dfs(to, x)
    return dist
        
s = dfs(0)
max_dist = max(s)
max_dist_idx = dist.index(max_dist)

dist[max_dist_idx] = 0
t = dfs(max_dist_idx)

print(max(t) + 1)




    
    