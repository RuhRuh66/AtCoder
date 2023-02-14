N = int(input())
A = list(map(int, input().split()))

sums = sum(A)
wa = 0
ans = 0
mod = 10**9 + 7

for i in range(N):
    wa += A[i]
    ans += (A[i] * (sums - wa)) % mod
    
print(ans%mod)