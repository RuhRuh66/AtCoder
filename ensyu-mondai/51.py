x, y = map(int, input().split())

mod = 1000000007
def comb(a, b):
    numer = 1
    for i in range(a+b, b, -1):
        numer = (numer*i) % mod
        
    denom = 1
    for j in range(a, 1, -1):
        denom = (denom*j) % mod
        
    ans = (numer*pow(denom, -1, mod)) % mod
    return ans 


print(comb(x, y))