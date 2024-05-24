H, W = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(10)]
A = [list(map(int, input().split())) for _ in range(H)]


for k in range(10):
    for i in range(10):
        for j in range(10):
            C[i][j] = min(C[i][j], C[i][k]+C[k][j])


dist_to_1 = [0]*10
for i in range(10):
    dist_to_1[i] = C[i][1]

ans = 0
for m in range(H):
    for n in range(W):
        if A[m][n] != -1:
            ans += dist_to_1[A[m][n]]
            
print(ans)
        



    

