N = int(input())
H = [0] + list(map(int, input().split()))

DP = [0] * (N+1)
DP[2] = DP[1] + abs(H[2]-H[1])
for i in range(3, N+1):
    DP[i] = min(DP[i-2]+abs(H[i]-H[i-2]), DP[i-1]+abs(H[i]-H[i-1]))
    
print(DP[N])