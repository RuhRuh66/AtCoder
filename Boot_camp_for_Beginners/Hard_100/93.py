import sys
sys.setrecursionlimit(10**8)

N = int(input())

G = [[] for i in range(N)]
for i in range(N-1):
    a, b, c = map(int,input().split())
    G[a-1].append((b-1,c))
    G[b-1].append((a-1, c))

q = []
Q, K = map(int, input().split())
for j in range(Q):
    x, y = map(int,input().split())
    q.append((x-1, y-1))
    

dists = [-1] * N
dists[K-1] = 0

def dfs(u, d, v):
    dists[u] = d
    for n, c in G[u]:
        if n == v:
            continue
        
        dfs(n, d+c, u)
dfs(K-1, 0, -1)

for j in range(Q):
    a, b = q[j]
    print(dists[a] + dists[b]) 
    