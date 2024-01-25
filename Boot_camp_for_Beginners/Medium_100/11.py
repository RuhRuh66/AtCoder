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
    temp = 10**10
    for l in range(M):
        c, d = C[l]

        temp = min(temp, (abs(a-c) + abs(b-d)))
        print(temp) 


