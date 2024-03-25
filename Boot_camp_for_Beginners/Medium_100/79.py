N, M = map(int, input().split())

if abs(N-M) >1:
    ans = 0
else:
    if N<M:
        N, M = M, N

    mod = 10**9+7

    temp1 = 1
    for i in range(1, N+1):
        temp1 = (temp1 * i) % mod
        
    temp2 = 1
    for i in range(1, M+1):
        temp2 = (temp2 * i) % mod
        
    if N == M:
        ans = (temp1 * temp2 * 2) % mod
    else:
        ans = (temp1 * temp2) % mod

print(ans)