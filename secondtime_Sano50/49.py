def eratosthenes(N):
    primes = [True] * (N+1)
    primes[0] = False
    primes[1] = False
    
    min_prime = [1] * (N+1)
    min_prime[2] = 2
    
    for i in range(2*2, N+1, 2):
        primes[i] = False
        min_prime[i] = 2
        
    for j in range(3, N+1):
        if primes[j] == True:
            min_prime[j] = j
            for k in range(j*2, N, j):
                primes[k] = False
                min_prime[k] =  j
    
    return min_prime

s = eratosthenes(10**6)
  

def factorization(x):
    nums = set()
    while x > 1:
        p = s[x]
        nums.add(p)
        x //= p
    return nums

N = int(input())

A = list(map(int, input().split()))

from math import gcd

seen = [0] * (10**6+5)

flag = True
for i in range(N):
    k = factorization(A[i])
    for x in k:
        if seen[x] == 0:
            seen[x] = 1
        else:
            flag = False
if flag == True:
    print('pairwise coprime')
    
else:
    g = A[0]
    for i in range(1,N):
        g = gcd(g, A[i])
    
    if g == 1:
        print('setwise coprime')
    else:
        print('not coprime')
        
    
        
     
    