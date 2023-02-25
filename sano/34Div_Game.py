N = int(input())

def prime_factorize(x):
    primes = []
    if x == 1:
        return []
    while x % 2 == 0:
        primes.append(2)
        x //= 2
        
    i = 3
    while i*i <= x:
        if x % i == 0:
            primes.append(i)
            x //= i
        else:
            i += 2
    if x != 1:
        primes.append(x)
        
        
    return primes

s = prime_factorize(N)

s = set(s)

ans = 0
for i in s:
    for e in range(1, 40):
        z = i**e
        if N % z == 0:
            ans += 1
            N//=z

print(ans)       
            
        
        
            
