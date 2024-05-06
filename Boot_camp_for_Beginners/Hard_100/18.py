sx, sy, gx, gy = map(int,input().split())

inf = 10**4

M = [[-1] * 2001 for _ in range(2001)]
visited = [[False] * 2001 for _ in range(2001)]
C = [[0] * 2001 for _ in range(2001)]

from collections import deque
que = deque()

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

que.append((sy, sx))
visited[sy][sx] = True
while que:
    y, x = que.popleft()
    if y == gy and x == gx:
        break
    for i in range(4):
        n_y = y + dy[i]
        n_x = x + dx[i]
        if -2000 <= n_y <= 2000 and -2000 <= n_x <= 2000:
            if visited[n_y][n_x] == False:
                visited[n_y][n_x] = True
                C[n_y][n_x] = C[y][x] + 1
                que.append((n_y, n_x))
print(C[gy][gx])

