def prime(N):
    is_prime = [True] * (N+1)
    is_prime[0] = False
    is_prime[1] = False
    
    
    
    for i in range(2*2, N+1, 2):
        is_prime[i] = False
        
    for j in range(3, N+1, 2):
        if is_prime[j] == True:
            for k in range(j*2, N+1, j):
                is_prime[k] = False
                
    primes = enumerate(is_prime)
    
    return primes

N = int(input())

a = [i for i, j in prime(N) if j == True]
print(*a)


    
