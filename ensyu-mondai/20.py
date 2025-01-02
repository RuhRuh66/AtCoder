N = int(input())
A = list(map(int, input().split()))


DP = [[0] * 1001 for _ in range(6)]

DP[0][0] = 1



for i in range(N):
    num = A[i]
    for j in range(5, 0, -1):
        for k in range(1000, num-1, -1):
            DP[j][k] += DP[j-1][k-num]

print(DP[5][1000])