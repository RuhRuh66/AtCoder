H = int(input())

import math


count = 0

def func(n):
    if n == 0:
        return 1
    else:
        return func(n-1) + 2**n
    

print(func(int(math.log2(H))))
    