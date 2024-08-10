import sys
sys.setrecursionlimit(10**8)

class Tree():
    def __init__(self, to, id):
        self.to = to
        self.id = id

N = int(input())
G = [[] for i in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(Tree(b-1, i))
    G[b-1].append(Tree(a-1, i))

C = [-1] * (N-1)

def dfs(u, prev_col, prev):
    k = 1
    for temp in G[u]:
        v, id = temp.to, temp.id
        if v == prev:
            continue
        if k == prev_col:
            k += 1
        C[id] = k
        dfs(v, k, u)
        k += 1
dfs(0, -1, -1)

print(max(C), *C)
            
        



