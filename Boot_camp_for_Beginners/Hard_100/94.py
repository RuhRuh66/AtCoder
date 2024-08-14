from math import comb

mod = 10**9 + 7

N, K = map(int, input().split())

if K == 1:
    print(N)
    exit()
    
for i in range(1, K+1):
    if N-K+1 < i:
        print(0)
    else:
        a = comb(N-K+1, i) % mod
        b = comb(K-1, i-1) % mod
        temp = (a*b) % mod
        print(temp)
        


   
   
   
   
   