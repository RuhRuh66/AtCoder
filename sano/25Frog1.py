N = int(input())
h = list(map(int, input().split()))

DP = [0] * N
DP[0] = 0
DP[1] = abs(h[1]-h[0])

for i in range(2, N):
    DP[i] = min(DP[i-2]+abs(h[i]-h[i-2]), DP[i-1]+abs(h[i]-h[i-1]))

print(DP[N-1])