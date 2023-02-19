N = int(input())

def prime_factorization(n):
    primes = []
    if n == 1:
        return []
    i = 2
    while n%2 == 0:
        primes.append(2)
        n //= 2
    i = 3
    while i*i <= n:
        if n % i == 0:
            primes.append(i)
            n //= i
        else:
            i += 2
    if n != 1:
        primes.append(n)        
    return set(primes)

s = prime_factorization(N)

ans = 0
for p in s:
    for e in range(1, 10**10):
        if N%(p**e) == 0:
            ans += 1
            N /=(p**e)
        else:
            break
print(ans)