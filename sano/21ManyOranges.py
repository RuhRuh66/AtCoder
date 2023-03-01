A, B, W = map(int, input().split())

import math

upper = math.floor(W*1000/A)
lower = math.ceil(W*1000/B)

if upper < lower:
    print('UNSATISFIABLE')
    
else:
    print(lower, upper)