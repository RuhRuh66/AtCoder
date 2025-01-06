N = int(input())
A = list(map(int, input().split()))

DP = [[0]* (1001) for _ in range(6)]
DP[0][0] = 1

for num in range(N):
    for card in range(6):
                    