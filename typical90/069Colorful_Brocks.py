N, K = map(int, input().split())

mod = 10**9 + 7


if N == 1:
    ans = K
    print(ans)
    exit()
elif N == 2:
    if K == 1:
        ans = 0
    else:
        ans = (K * (K-1)) % mod
        print(ans)
        exit()
else:
    if K== 1 or K == 2:
        ans = 0
        
    else:
        ans = (K * (K-1) *(pow(K-2, N-2, mod)))  % mod
        
print(ans)