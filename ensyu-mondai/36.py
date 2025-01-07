from math import pi, cos, sqrt

A, B, H, M = map(int, input().split())

c = sqrt(A**2 + B**2 - 2*A*B*cos(((H*60+M)/720-M/60)*2*pi))

print(c)