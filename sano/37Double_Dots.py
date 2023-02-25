N, M = map(int, input().split())
routs = [[] for i in range(N+1)]
for j in range(M):
    A, B = map(int, input().split())
    routs[A].append(B)
    routs[B].append(A)

    
from collections import deque

s = deque()
visited = [False] * (N+1)
mark = [-1] * (N+1)

now_room = 1
visited[now_room] = True
s.append(now_room)

while len(s) > 0:
    now_room = s.popleft()
    next_rooms = routs[now_room]
    for i in next_rooms:
        if visited[i] == False:
            visited[i] = True
            mark[i] = now_room
            s.append(i)
            
        
print('Yes')
for i in mark[2:]:
    print(i)