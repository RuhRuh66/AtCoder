import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
A = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    A[a].append(b)
    A[b].append(a)
    
for j in A:
    j.sort()


visited = [False] * N
def rec(v, Gv, seen):

    seen[v] = True

    
    for n in Gv[v]:
        if seen[n] == True:
            continue
        rec(n, Gv, seen)
        
    return 
 
rec(0, A, visited)
cnt = 1
for i in range(N):
    if visited[i] == False:
        rec(i, A, visited)
        cnt += 1
        
print(cnt)
        
    
    
    