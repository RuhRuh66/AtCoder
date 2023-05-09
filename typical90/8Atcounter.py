n = int(input())
s = str(input())

atcoder = 'atcoder'
mod = 10**9+7

DP = [[0] * 8 for i in range(n+1)]

for i in range(n+1):
    DP[i][0] = 1
    
for i in range(n):
    for j in range(len(atcoder)):
        DP[i+1][j+1] = DP[i][j+1]
        if s[i] == atcoder[j]:
            DP[i+1][j+1] += DP[i][j]
            
print(DP[n][7] % mod)


