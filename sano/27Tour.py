N, M = map(int, input().split())

roads = [[] for i in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    roads[A].append(B)
    
from collections import deque



count = 0
for i in range(N):
    count_i = 1
    visited = [0] * N
    que = deque()
    now_city = i
    visited[now_city] = 1
    que.append(now_city)
    while len(que)>0:
        start = que.popleft()
        for j in roads[start]:
            if visited[j] == 0:
                visited[j] = 1
                que.append(j)
                count_i += 1
    count += count_i
 
print(count)           
        
    
    