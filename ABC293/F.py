t = int(input())

from math import log2, floor

def check(num_10, n):
    if n == 1:
        return False
    while num_10:
        if num_10 % n > 2:
            return False
        num_10 //= n
    return True

for _ in range(t):
    n = int(input())
    cnt = 0
    good_int_temp = set()
    good_int_temp.add(n)
    good_int_temp.add(n-1)
    d_max = floor(log2(10**18))+1
    
    for i in range(2, d_max):
        x = int(n**(1/i))
    
    

