N, W = map(int, input().split())

DP = [0] * (W+1)

for i in range(N):
    w, v = map(int, input().split())
    for j in range(W, w-1, -1):
        DP[j] = max(DP[j], DP[j-w]+v)
        
print(DP[W])

