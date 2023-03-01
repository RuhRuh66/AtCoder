N =int(input()) 

import math
n = int(math.sqrt(N))+1
m = int(math.log2(N))+1

A = set()

for i in range(2, n):
    for j in range(2, m):
        if i ** j <= N:
            A.add(i**j)

print(N-len(A))


