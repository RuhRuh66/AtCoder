from collections import defaultdict

def eratosthenes_fact(N):
    n = int(N ** 0.5) + 1
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False
    
    for i in range(2*2, n+1, 2):
        is_prime[i] = False
        
    for i in range(3, n+1, 2):
        if is_prime[i] == True:
            for j in range(i*2, n+1, i):
                is_prime[j] = False
                
    
    primes = [x for x, y in enumerate(is_prime) if y == True]
    
    facts = defaultdict(int)
    
    for k in primes:
        while N % k == 0:
            facts[k] += 1
            N //= k
            
    if N != 1:
        facts[N] += 1
    
    return facts


    
ans = []
N = int(input())
for key, value in eratosthenes_fact(N).items():
    ans += ([key] * value)
    
print(*ans)
