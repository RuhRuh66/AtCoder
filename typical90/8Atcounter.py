N = int(input())
S = [0]+list(input())

T = '0atcoder'
mod = 10**9 +7

DP = [[0]*8 for i in range(N+1)]
DP[0][0] = 1
for i in range(1, N+1):
    DP[i][0] = 1

for i in range(1, N+1):
    for j in range(1, len(T)):
        DP[i][j] = DP[i-1][j]
        if S[i] == T[j]:
            DP[i][j] = DP[i-1][j-1] + DP[i-1][j]
            
print((DP[N][7])%mod)