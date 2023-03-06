n, a, b = map(int, input().split())
mod = 10**9 +7

import math

def nCr_mod(n, r, mod):
    numerator = 1
    for i in range(n, n-r, -1):
        numerator *= i
        numerator %= mod
    denominator = 1
    for j in range(r,0,-1):
        denominator *= j
        denominator %= mod
        
    denominatior_inv = pow(denominator, -1, mod)
    
    return  (numerator * denominatior_inv) % mod


comb_a = nCr_mod(n, a, mod)
comb_b = nCr_mod(n, b, mod)

ans = (pow(2, n, mod) - comb_a -comb_b -1) % mod

print(ans)