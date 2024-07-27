H, W = map(int, input().split())
A = [[] for i in range(H)]
for i in range(H):
    temp = list(input())
    A[i] = temp

    
from collections import deque

B = deque()
distance = [[-1]*W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if A[i][j] == '#':
            B.append((i,j))
            distance[i][j] = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while B:
    x, y = B.popleft()
    for i in range(4):
        n_x = x + dx[i]
        n_y = y + dy[i]
        if 0<= n_x < H and 0<= n_y < W and distance[n_x][n_y] == -1:
            distance[n_x][n_y] = distance[x][y] + 1
            B.append((n_x, n_y))

ans = 0   
for i in range(H):
    ans = max(ans, max(distance[i]))

print(ans)
        




        
    

