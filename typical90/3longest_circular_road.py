import sys
sys.setrecursionlimit(10**6)

N  = int(input())
dest = [[] for i in range(N)]
for i in range(1, N):
    A, B = map(int, input().split())
    A -= 1
    B -= 1

    dest[A].append(B)
    dest[B].append(A)
    
distance = [0] * N
visited = [False] * N

def dfs(x, last=-1):
    visited[x] = True
    for to in dest[x]:
        if visited[to] == True:
            continue

x        distance[to] = distance[x] + 1
        dfs(to, x)


