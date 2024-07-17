N, K = map(int, input().split())

if K == 0:
    print(N*N)
    exit()



ans = 0
for b in range(K+1, N+1):
    n = N//b
    m = N%b
    ans += (b-K)* n + max(0, m-K+1)

print(ans) 
