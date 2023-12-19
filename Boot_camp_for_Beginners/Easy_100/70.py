X = int(input())

dp = [False] * (X+1+105)

dp[0] = True

for i in range(0, X+1):
    for j in range(100, 106):
        if dp[i] == True:
            dp[i+j] = True

if dp[X]:
    print(1)
else:
    print(0)