N = int(input())
H = list(map(int, input().split()))

DP = [10**9] * N
DP[0] = 0
DP[1] = abs(H[1] - H[0])

for i in range(2, N):
    DP[i] = min(DP[i-2]+abs(H[i]-H[i-2]), DP[i-1] + abs(H[i]-H[i-1]))
    
print(DP[N-1])