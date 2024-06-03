H, W = map(int, input().split())
M = [str(input()) for _ in range(H)]

score = [[10**6] * W for i in range(H)]
score[0][0] = 0

from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque()
start = (0, 0)

q.append(start)

while q:
    x, y = q.popleft()
    for i in range(4):
        n_x, n_y = x+dx[i], y+dy[i]
        if 0<=n_x<H and 0<=n_y<W and M[n_x][n_y] == '.' and score[n_x][n_y] > score[x][y]+1:
            score[n_x][n_y] = score[x][y] + 1
            if n_x == H-1 and n_y == W-1:
                q.clear()
                break
            q.append((n_x, n_y))

if score[H-1][W-1] == 10**6:
    print(-1)
    exit()
    

black = 0
for j in range(H):
    black += M[j].count('#')

ans = W*H - black - score[H-1][W-1]-1
print(ans)