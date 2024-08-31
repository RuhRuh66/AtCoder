

def eratosthenes(N):
    prime = [True] * (N+1)
    prime[0] = False
    prime[1] = False
    if N >= 4:
        for i in range(4, N+1, 2):
            prime[i] = False
            
        k = 3
        while k*k <= N:
            if prime[k] == True:
                for t in range(2*k, N+1, k):
                    prime[t] = False
            else:
                pass
            k += 1
            
    lis = [x for x, t in enumerate(prime) if t == True]
    return lis
            
N = int(input())

sam = eratosthenes(N)   
from collections import defaultdict

fac = defaultdict(int)

for n in sam:
    while N > 1:
        if N % n == 0:
            fac[n] += 1
            N //= n
        else:
            break

cnt = 0

for x, y  in fac.items():
    i = 1
    while y-i >= 0:
        y -= i
        cnt += 1
        i += 1
        
print(cnt)
            
            

        

 
        
    
    
    