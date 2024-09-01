N = int(input())
from collections import defaultdict

p = defaultdict(int)

i = 2

while i*i <= N:
    while N % i == 0:
        p[i] += 1
        N //= i
    i += 1
    
        
if N != 1:
    p[N] += 1
    
cnt = 0

for i, j in p.items():
    k = 1
    while j>0:
        cnt +=1
        k += 1
        j -= k
        

print(cnt)
        

        

 
        
    
    
    