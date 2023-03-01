N, W = map(int, input().split())
A = []
for i in range(N):
    temp = list(map(int, input().split()))
    A.append(temp)
    

DP = [[0] * (W+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(W+1):
        DP[i][j] = DP[i-1][j]
        if j-A[i-1][0] >= 0:
            DP[i][j] = max(DP[i][j], DP[i-1][j-A[i-1][0]] + A[i-1][1])
            
print(DP[N][W])