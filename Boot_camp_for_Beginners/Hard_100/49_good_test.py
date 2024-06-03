n, a, b = map(int, input().split())

mod = 10**9+7

fact = {}
fact[n] = n
fact[n-1] = (fact[n] * (n-1) ) % mod

inv_fact = [0] * (max(a, b) + 1)
inv_fact[1] = 1

for i in range(2, max(a, b) +1):
    fact[n-i] = fact[n-i+1] * (n-i) % mod
    inv_fact[i] = inv_fact[i-1] * pow(i, -1, mod) % mod
    
total = pow(2, n, mod)

ans = (total - 1 - fact[n-a+1] * inv_fact[a] - fact[n-b+1] * inv_fact[b]) % mod

print(ans)
    
    