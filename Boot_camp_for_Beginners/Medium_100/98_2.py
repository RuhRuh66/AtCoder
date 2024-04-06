def Prime_find(n):
    i = 2
    primes = {}
    
    while i * i <= n:
        cnt = 0
        while n % i == 0:
            n //= i
            cnt += 1
        primes[i] = cnt
        i += 1
        
    if n != 1:
        primes[n] = 1
        
    return primes


N, P = map(int, input().split())

d = Prime_find(P)

ans = 1
for i  in d:
    ans *= i**(d[i]//N)

print(ans)
    
        
