N, K = map(int, input().split())
S = input()

DP = [[N+10] * 26 for _ in range(N+1)]

for i in range(N-1, -1, -1):
    for j in range(26):
        DP[i][j] = DP[i+1][j]
        
    DP[i][ord(S[i])-ord('a')] = i
    
res = ''

j = -1

for i in range(K):
    for ordc in range(26):
        k = DP[j+1][ordc]
        
        if k <= N-K+i:
            res += chr(ord('a')+ordc)
            j = k
            break
print(res)
        