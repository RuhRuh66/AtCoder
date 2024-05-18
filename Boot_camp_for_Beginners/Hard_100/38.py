H, W = map(int, input().split())
M = [[]for i in range(H)]

for i in range(H):
    temp = list(input())
    M[i] = temp

from collections import deque

def dps(x, y):
    ans = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    wd = [[-1]*W for _ in range(H)]
    que = deque()
    wd[x][y] = 0
    que.append((x, y))
    while que:
        x, y = que.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0<=new_x<H and 0 <= new_y < W and M[new_x][new_y] == '.' and wd[new_x][new_y] == -1:
                wd[new_x][new_y] = wd[x][y] + 1
                que.append((new_x, new_y))
    for i in wd:
        ans = max(ans, max(i))
    
    return ans

ans = 0
for i in range(H):
    for j in range(W):
        if M[i][j] == '.':
            ans = max(ans, dps(i, j))

print(ans)



                
            
            
    
                    
                