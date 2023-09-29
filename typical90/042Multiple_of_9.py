K = int(input())
mod = 10**9 + 7

if K % 9 != 0:
    print(0)
    exit()

DP = [0] * (K+1)
DP[0] = 1

for i in range(1, K+1):
    for j in range(1, 10):
        if i - j >= 0:
            DP[i] += DP[i-j]

print(DP[K] % mod)