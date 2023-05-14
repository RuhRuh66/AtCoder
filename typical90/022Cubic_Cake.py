import math

A, B, C = map(int, input().split())

D = math.gcd(A, B)
E = math.gcd(D, C)

print((A+B+C)//E - 3)