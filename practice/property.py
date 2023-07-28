import sys
sys.setrecursionlimit(10**6)

H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]

def get_num(x, y, W):
    return x*W + y

tree = [[] for _ in range(H*W)]

move = [(0, 1), (-1, 0), (0, -1), (1, 0)]

for i in range(H):
    for j in range(W):
        if A[i][j] == '.':
            continue
        for dx, dy in move:
            ni, nj = i + dx, j + dy
            if 0<=ni<H and 0<=nj<W and A[ni][nj] == '#':
                tree[get_num(i, j, W)].append(get_num(ni, nj, W))
    

visited = [False] * (H*W)


def rec(v, dv, seen):
    seen[v] = True
    for j in dv[v]:
        if seen[j] == True:
            continue
        rec(j, dv, seen)
    return

ans = 0
for i in range(H):
    for j in range(W):
        if A[i][j] == '.':
            continue
        if visited[get_num(i, j, W)] == True:
            continue
        
        ans += 1
        rec(get_num(i, j, W), tree, visited)

        
print(ans)
    
