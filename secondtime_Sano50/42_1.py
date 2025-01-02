N, W = map(int, input().split())
items = [[0, 0]]
for i in range(N):
    w, v = map(int, input().split())
    items.append([w, v])

DP = [[0] * (W+1) for _ in range(N+1)]

for j in range(1, N+1):
    for k in range(W+1):
        w, v = items[j]
        DP[j][k] = max(DP[j][k], DP[j-1][k])
        if k - w >= 0:
            DP[j][k] = max(DP[j][k], DP[j-1][k-w] + v)
            
        
print(DP)