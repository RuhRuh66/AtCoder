H, N = map(int, input().split())
M = []
for i in range(N):
   a, b = map(int, input().split())
   M.append((a, b)) 
   
inf = 10 ** 9
DP = [[inf] * (H+1) for _ in range(N+1)]

DP[0][0] = 0
for i in range(N):
    DP[i+1][:] = DP[i][:]
    for h in range(H):
        a, b = M[i]
        if DP[i][h] != inf or DP[i+1][h] != inf:
            DP[i+1][min(h+a, H)] = min(DP[i+1][h]+b, DP[i+1][min(h+a, H)])

print(DP[N][H])