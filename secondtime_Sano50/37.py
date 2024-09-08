N, M = map(int, input().split())
rout = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    rout[a].append(b)
    rout[b].append(a)
    
from collections import deque

q = deque()
q.append(1)
visited = [False] * (N+1)
mark = [0] * (N+1)

visited[1] = True

while q:
    now = q.popleft()
    for t in rout[now]:
        if visited[t] == False:
            mark[t] = now
            visited[t] = True
            q.append(t)
print('Yes')
for i in range(2, N+1):
    print(mark[i])
            
 
            
    
    
    
