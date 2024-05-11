from collections import defaultdict

def factorization(n):
    F = defaultdict(int)
    f = 0
    while n%2 ==0:
         f += 1
         n //= 2
         
    F[2] += f
    
    i = 3
    while i * i <= n:
        f = 0
        while n % i == 0:
            f += 1
            n //= i
        if f != 0:
            F[i] += f 
        i += 1
    if n != 1:
        F[n] += 1
    return F

mod = 10**9+7

N = int(input())

fac = defaultdict(int)
for i in range(2, N+1):
    divs = 1
    temp = factorization(i)
    for a, b in temp.items():
        fac[a] += b
ans = 1
for v in fac.values():
    ans *= (v+1) % mod
    
print(ans%mod)       
    

            
        
        