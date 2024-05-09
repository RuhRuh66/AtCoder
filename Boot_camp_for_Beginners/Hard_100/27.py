N, Q = map(int, input().split())
Tree = [[] for i in range(N)]

for i in range(N-1):
    a, b = map(int, input().split())
    Tree[a-1].append(b-1)
    Tree[b-1].append(a-1)
    

ans = [0] * N
visited = [False] * N


for j in range(Q):
    p, x = map(int, input().split())
    ans[p-1] += x

from collections import deque
que = deque()

que.append(0)
visited[0] = True
while que:
    now = que.popleft()
    for k in Tree[now]:
        if visited[k] == False:
            ans[k] += ans[now]
            visited[k] = True
            que.append(k)

print(*ans)
