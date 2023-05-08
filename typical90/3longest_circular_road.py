import sys
sys.setrecursionlimit(10**6)

N = int(input())

edges = [[] for i in range(N)]

for i in range(N-1):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    edges[x].append(y)
    edges[y].append(x)
    

dist = [0] * N


def dfs(x, last=-1):
    global dist
    for to in edges[x]:
        if to == last:
            continue
        dist[to] = dist[x] + 1
        dfs(to, x)
        
dfs(0)
max_dist = max(dist)
farest = dist.index(max_dist)

dist[farest] = 0
dfs(farest)

print(max(dist)+1)



            
        

    
    
    

    

                