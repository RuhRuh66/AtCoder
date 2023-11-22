N, M = map(int, input().split())

A = [[] for i in range(N)]

for j in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    A[a].append(b)
    A[b].append(a)
    
for k in range(N):
    print(len(A[k]))
    