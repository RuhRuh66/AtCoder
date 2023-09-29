h, w = map(int, input().split())
rs, cs = map(int, input().split())
rt, ct = map(int, input().split())
s = [input() for i in range(h)]

check = [[[10**10]*w for _ in range(h)] for _ in range(4)]
for i in range(4):
    check[i][rs-1][cs-1] = 0
    
from collections import deque
que = deque([(rs-1, cs-1, 0), (rs-1, cs-1, 1), (rs-1, cs-1, 2), (rs-1, cs-1, 3)])
move = [(0, 1), (-1, 0), (0, -1), (1, 0)]

while que:
    r, c, direction = que.popleft()
    dd = check[direction][r][c]
    for i in range(4):
        if check[i][r][c] <= dd + 1:
            continue
        check[i][r][c] = dd + 1
        que.append((r, c, i))
    dr, dc = move[direction]
    next_r = r + dr
    next_c = c + dc
    
    if 0<= next_r <h and 0<= next_c < w and s[next_r][next_c] == '.' and  check[direction][next_r][next_c] < dd


        
        
    
    
    
