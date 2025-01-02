H, W = map(int, input().split())
S = [list(str(input())) for _ in range(H)]

from collections import deque

def wd(x, y):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    q = deque()
    dist = [[-1] * W for _ in range(H)]  
    dist[x][y] = 0
    q.append((x, y))
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx, ny = a+dx[i], b+dy[i]
            if 0<=nx < H and 0<= ny < W and S[nx][ny] == '.' and dist[nx][ny] == -1:
                dist[nx][ny] = dist[a][b] + 1
                q.append((nx, ny))
    temp = 0        
    for j in range(H):
        temp = max(temp, max(dist[j]))
    
    return temp

ans = 0
for k in range(H):
    for l in range(W):
        if S[k][l] == '.':
            temp2 = wd(k,l)
            ans = max(ans, temp2)
        
        
