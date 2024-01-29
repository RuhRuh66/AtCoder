N, M  = map(int, input().split())

A = []
C = []


for i in range(N):
    a, b = map(int, input().split())
    A.append([a, b])
for j in range(M):
    c, d = map(int, input().split())
    C.append([c, d])
    
for k in range(N):
    a, b = A[k]
    E = {}
    for l in range(M):
        c, d = C[l]
        dist = abs(a-c) +abs(b-d)
        E[l] = dist
    F = sorted(E.items(), key= lambda x: x[1])
    print(F[0][0]+1)
        

