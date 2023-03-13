H, W = map(int, input().split())
A = []
for i in range(H):
    temp = list(map(int, input().split()))
    A.append(temp)


L = [sum(A[i]) for i in range(H)]
C = []
for i in range(W):
    cnt = 0
    for j in range(H):
        cnt += A[j][i]
    C.append(cnt)
    
    
B = [[0]*W for i in range(H)]
for i in range(H):
    for j in range(W):
        B[i][j] = L[i] + C[j] - A[i][j]
        
for i in range(H):
    print(*B[i])

