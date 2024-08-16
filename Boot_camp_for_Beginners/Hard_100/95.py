N = int(input())
A = list(map(int, input().split()))

mod = 10**9 + 7
ans = 0
for i in range(60):
    zeros = 0
    for j in range(N):
        if (A[j]>>i) & 1 == 0:
            zeros += 1
            
    ans += pow(2, i , mod) * zeros * (N-zeros)
    ans %= mod
    
print(ans)