N = int(input())
from math import log10

c = 0

temp = 0
while c*c <=N:
    c += 1
    if N % c == 0:
        temp = c
        
temp2 = N//temp
ans = max(temp, temp2)
print(int(log10(ans))+1)