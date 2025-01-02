N = int(input())
A = list(map(int, input().split()))

mod = 10**9 + 7

s = sum(A) % mod

total = pow(s, 2, mod)


for i in range(N):
    temp = pow(A[i], 2, mod)
    total -= temp
    if total < 0:
        total += mod

p_inv = pow(2, -1, mod)

ans = (total * p_inv) % mod
print(ans)


