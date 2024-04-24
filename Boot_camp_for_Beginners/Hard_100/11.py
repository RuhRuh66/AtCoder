A, B = map(int, input().split())

from math import gcd

C = gcd(A, B)

from collections import defaultdict

D = defaultdict(int)

while C % 2 == 0:
    D[2] += 1
    C //= 2

i = 3
while i * i <= C:
    while C % i == 0:
        D[i] += 1
        C //= i
    i += 2
if C!= 1:
    D[C] += 1
    
print(len(D)+1)
        