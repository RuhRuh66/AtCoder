H, W = map(int, input().split())

from math import ceil

if H == 1:
    ans = W
elif W == 1:
    ans =  H
    
else:
    ans = ceil(H/2) * ceil(W/2)

print(ans)