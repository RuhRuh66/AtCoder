S = int(input())

max_num = S//3

import math

if S==1 or S ==2:
    print(0)
    exit()
    
mod = 10**9+7
ans = 0
for i in range(1, S//3+1):
    amari = S - i*3
    coms = math.comb(amari+i-1, i-1) % mod
    ans += coms

print(ans%mod)