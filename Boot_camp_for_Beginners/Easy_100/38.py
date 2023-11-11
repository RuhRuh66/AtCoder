from math import ceil

rest = 0
sums = 0
for i in range(5):
    a = int(input())
    temp = ceil(a/10)*10
    rest = max(rest, temp-a)
    sums += temp
    
print(sums-rest)
    
    
    
    