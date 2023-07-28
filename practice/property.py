import sys
sys.setrecursionlimit(10**6)

H, W = map(int, input().split())

A = [list(input()) for _ in range(H)]

move = [(0, 1), (-1, 0), (0, -1), (1, 0)]

grid = [[] for i in range(H*W)]

def getnum(x, y, H, W):
    return x*W + y

def rec(v, dv, seen):
    seen[v] = True
    for n in dv[v]:
        if seen[n] == True:
            continue
        rec(n, dv, seen)
    return
    
def makegrid(A, grid, H, W, move):
    for i in range(H):
        for j in range(W):
            if A[i][j] == '.':
                continue
            for dx, dy in move:
                nx, ny = i+dx, j+dy
                if 0<= nx <H and 0 <= ny < W and A[nx][ny] == '#':
                    grid[getnum(i, j, H, W)].append(getnum(nx, ny, H, W))
    return grid
                    
visited = [False] * (H*W)

dv = makegrid(A, grid, H , W, move)

for i in range(H):
    for j in range(W):
        if A[i][j] == '.':
            continue
        rec(getnum(i, j, H, W), dv, visited)

print(visited)
        
