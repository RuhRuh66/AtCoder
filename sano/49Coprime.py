N = int(input())
A = list(map(int, input().split()))

D = [0] * (10**6+10)

for i in range(2, 10**6+10):
    if D[i] != 0:
        continue
    for j in range(1, 10**6):
        if i * j < 10**6 +10:
            if D[i*j] == 0:
                D[i*j] = i
        else:
            break

def fact_prime_fact(x):
    prime = []
    while x > 1:
        prime.append(D[x])
        x //= D[x]
    return prime

pairwise = True
prime_used = [0] * 10**6
for i in range(N):
    s = fact_prime_fact(A[i])
    s = set(s)
    for j in s:
        if prime_used[j] != 0:
            pairwise = False
            break
        else:
            prime_used[j] = 1
if pairwise == True:
    print('pairwise coprime')
    exit()
    
from math import gcd
g = A[0]
for k in range(1, N):
    g = gcd(g, A[k])
if g == 1:
    print('setwise coprime')
    exit()
    
print('not coprime')
            



 
    

