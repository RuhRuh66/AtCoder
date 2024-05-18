S = int(input())

x1 = 0
y1 = 0
x2 = 10**9
y2 = 1
x3 = int()
y3 = int()

from math import ceil

y3 = ceil(S/(10**9))
x3 = (10**9)*y3 - S 

print(x1, y1, x2, y2, x3, y3)