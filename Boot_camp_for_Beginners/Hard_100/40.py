S = input()
l = len(S)
A = S.replace('x', '')
B = ''.join(reversed(A))

if A != B:
    print(-1)
    exit()
    
else:
    C = ''.join(reversed(S))
    dp = [[10*9]*(l+1) for _ in range(l+1)]
    
    
    for i in range(l+1):
        dp[0][i] = i
        dp[i][0] = i
    
    for j in range(1, l+1):
        for k in range(1, l+1):
            if S[j-1] == C[k-1]:
                dp[j][k] = min(dp[j-1][k-1], dp[j][k])
            else:
                dp[j][k] = min(dp[j-1][k]+1, dp[j][k-1]+1, dp[j][k])
            
    print(dp[l][l])