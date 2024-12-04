from math import lcm

N, X, Y = map(int, input().split())

a = N // X
b = N // Y

l = lcm(X, Y)

c = N // l

print(a+b-c)