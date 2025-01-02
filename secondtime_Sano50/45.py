N, a, b = map(int, input().split())
mod = 10**9+7

if N == 2:
    print(0)
    exit()


def comb(x, y):
    numerator = 1
    denominator = 1
    for i in range(y):
        numerator = (numerator * (x-i)) % mod
        denominator = (denominator * (y-i)) % mod
        
    inv = pow(denominator, -1, mod)
    return (numerator * inv) % mod



def pow_mod(x, n, mod):
    temp = 1
    while n >0:
        if n & 1 == 1:
            temp = temp * x % mod
        x = x**2 % mod
        n = n >> 1
    return temp



ans = pow_mod(2, N, mod) - comb(N, a) - comb(N, b) -1

while ans < 0:
    ans += mod
    
print(ans)