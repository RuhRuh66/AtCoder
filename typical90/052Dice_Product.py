N = int(input())
mod = 10**9+7
A = []
for i in range(N):
    ans = sum(list(map(int, input().split())))
    A.append(ans)

multi = 1
for i in range(N):
    multi *= A[i] % mod

print(multi%mod)

