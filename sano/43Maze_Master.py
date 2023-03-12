H, W = map(int, input().split())
routes = []
for i in range(H):
    temp = list(str(input()))
    routes.append(temp)

from collections import deque
    
for i in range(H):
    for j in range(W):
        if routes[i][j] == '#':
            continue
        
        counts = [[-1]*W for i in range(H)]
        s = deque()
        counts[i][j] = 0
        s.append([i, j])
        
        while len(s) > 0:
            
        
        
        