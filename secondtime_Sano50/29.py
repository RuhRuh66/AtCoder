N = int(input())
mod = 10**9 +7
total = pow(10, N, mod)
A = pow(9, N, mod)
B  =pow(8, N, mod)

ans = (total-2*A + B) % mod

print(ans)