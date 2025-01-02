S = int(input())


max_len = S//3

import math

mod = 10 ** 9 + 7

if S <= 2:
    print(0)
    exit()



ans = 0
for n in range(1, max_len+1):
    remain = S-3*n
    temp = (math.factorial(n-1+remain)//(math.factorial(remain)*math.factorial(n-1))) % mod
    
 
 
    ans += temp
    
    
print(ans % mod)
    
        

    
