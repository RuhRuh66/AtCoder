A, B = map(int, input().split())

from math import gcd
s = gcd(A, B)
print(A*B//s)

