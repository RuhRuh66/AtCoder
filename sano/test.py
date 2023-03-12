S = int(input())
mod = 10**9 + 7

DP = [0] * (S+1)

DP[1] = 0
DP[2] = 0
DP[3] = 1


for i in range(4, S+1):
    DP[i] = DP[i-1] + DP[i-3]

print(DP[S]%mod)

