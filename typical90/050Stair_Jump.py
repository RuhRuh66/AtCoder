N, L = map(int, input().split())

mod = 10**9+7

DP = [0] * (N+1) 
DP[0] = 1
DP[1] = 1

for i in range(2, N+1):
    if i - L >= 0:
        DP[i] = DP[i-1] + DP[i-L]
        
    else:
        DP[i] = DP[i-1]
        
print(DP[N]%mod)