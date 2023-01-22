H, N = map(int, input().split())
magics = []
for i in range(N):
    temp = list(map(int, input().split()))
    magics.append(temp)

inf = 10 ** 10
DP = [[inf] * (H+1) for i in range(N+1)]    
DP[0][0] = 0

for i in range(N):
    for j in range(H+1):
        if DP[i][j] == inf:
            continue
        
        DP[i+1][j] = min(DP[i][j], DP[i+1][j])

        if j + magics[i][0] >= H:
            DP[i+1][H] = DP[i][j] + magics[i][1]
        else:
            DP[i+1][j+magics[i][1]] = min(DP[i][j]+magics[i+1][1])


