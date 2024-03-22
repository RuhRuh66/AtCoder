N = int(input())
bottle_neck = 10**16

from math import ceil

for i in range(5):
    temp = int(input())
    bottle_neck = min(bottle_neck, temp)
    
wating = ceil(N / bottle_neck)
print(wating + 4)


