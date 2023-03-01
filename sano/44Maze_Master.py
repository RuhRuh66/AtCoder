from collections import deque
H, W = map(int, input().split())
routes = []
for i in range(H):
    temp = list(str(input()))
    routes.append(temp)
    
    
ans = 0
for i in range(H):
    for j in range(W):
        if routes[i][j] == '#':
            continue
        
        distance = [[-1] * W for i in range(H)]
        s = deque()
        distance[i][j] = 0
        s.append([i, j])
        
        while len(s)>0:
            h, w = s.popleft()
            for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                new_h, new_w = h+x, w+y
                if new_h <0 or new_w <0 or new_h >= H or new_w >= W:
                    continue
                else:
                    if routes[new_h][new_w] != '#' and distance[new_h][new_w] == -1:
                        distance[new_h][new_w] = distance[h][w]+1
                        s.append([new_h, new_w])
        for k in range(H):
            ans = max(ans, max(distance[k]))
            
print(ans)

                    
                
                
        