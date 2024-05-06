R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

sy -= 1
sx -= 1
gy -= 1
gx -= 1

M = []
for i in range(R):
    temp = list(input())
    M.append(temp)
    
costs = [[0]*C for _ in range(R)]
visited = [[False]*C for _ in range(R)]

from collections import deque
que = deque()

dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

costs[sy][sx] = 0
visited[sy][sx] = True
que.append((sy, sx))

while que:
    y, x = que.popleft()
    for i in range(4):
        n_y = y + dy[i]
        n_x = x + dx[i]
        if 0<= n_y <R and 0<= n_x <C and M[n_y][n_x] == '.':
            if visited[n_y][n_x] == False:
                visited[n_y][n_x] = True
                costs[n_y][n_x] = costs[y][x] + 1
                que.append((n_y, n_x))

print(costs[gy][gx])




 