N = int(input())
A = list(map(int, input().split()))

#DP[i][j] j=０：i日目に勉強した時の最大値。j=１：i日目に勉強しなかった場合の最大値。

DP = [[0] * 2 for _ in range(N+1)]

DP[1][0] = A[0]

for i in range(2, N+1):
    DP[i][0] = DP[i-1][1]+A[i-1]
    DP[i][1] = max(DP[i-1][0], DP[i-1][1])

    
print(max(DP[N][0], DP[N][1]))