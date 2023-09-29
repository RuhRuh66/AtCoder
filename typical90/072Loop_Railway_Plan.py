h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]

visited = [[False] * w for _ in range(h)]
ans = -1
def dfs(x, y, xs, ys, cnt):
    moves = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    global ans
    for dx, dy in moves:
        nx, ny = x+dx, y+dy
        if 0<=nx<h and 0<=ny<w and visited[nx][ny] == False and c[nx][ny] == '.':
            if nx == xs and ny == ys and cnt >3:
                ans = max(ans, cnt+1)
            else:
                visited[nx][ny] = True
                dfs(nx, ny, xs, ys, cnt+1)
                visited[nx][ny] = False
                
    

for i in range(h):
    for j in range(w):
        dfs(i, j, i, j, 0)
        
print(ans)
        