N, K = map(int, input().split())

if N % K == 0:
    print(0)
    exit()
    
ans = min(N%K, abs(N%K - K))

print(ans)