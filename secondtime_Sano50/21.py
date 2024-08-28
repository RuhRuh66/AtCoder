from math import floor, ceil

A, B, W = map(int, input().split())

upper = floor(1000*W/A)
lower = ceil(1000*W/B)

if upper < lower:
    print('UNSATISFIABLE')
else:
    print(lower, upper)