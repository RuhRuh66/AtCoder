R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
sy, sx = sy-1, sx-1
gy, gx = gy-1, gx-1

maze = [input() for _ in range(R)]


dir =  [(0, 1, 'r'), (1, 0, 'u'), (0, -1, 'l'), (-1, 0, 'd')]

dist = [[[-1, ''] for j in range(C)] for _ in range(R)]

dist[sy][sx] = [0, 's']

from collections import deque
q = deque()

q.append((sy, sx))

while q:
    now = q.popleft()
    for i in range(4):
        ny = now[0] + dir[i][0]
        nx = now[1] + dir[i][1]

        if dist[ny][nx][0] == -1 and maze[ny][nx] != '#':
            dist[ny][nx][0] = dist[now[0]][now[1]][0] + 1
            dist[ny][nx][1] = dir[i][2]
            q.append((ny, nx))
            
print(dist[gy][gx][0])


