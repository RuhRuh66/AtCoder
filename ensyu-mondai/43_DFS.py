import sys
sys.setrecursionlimit(1000000)

N, M = map(int, input().split())

ps = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    ps[a-1].append(b-1)
    ps[b-1].append(a-1)
    
    
seen = [False] * N
def dfs(ps, s):
    if seen[s] == True:
        return    
    seen[s] = True
   
    for t in ps[s]:
        dfs(ps, t)
   
    
    
k = dfs(ps, 0)

if all(seen):
    print('The graph is connected.')
else:
    print('The graph is not connected.')
    