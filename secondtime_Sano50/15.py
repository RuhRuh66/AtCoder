N = str(input())
K = len(N)

from collections import defaultdict

D = defaultdict(int)

r_sum = 0
for i in range(len(N)):
    d = int(N[i]) % 3
    D[d] += 1
    r_sum += d



    

if r_sum % 3 == 0:
    ans = 0
elif r_sum % 3 == 1:
    if D[1] >= 1:
        ans = 1
    elif D[2] >= 2:
        ans = 2
    else:
        ans = -1
        
else:
    if D[2] >= 1:
        ans = 1
    elif D[1] >= 2:
        ans = 2
    else:
        ans = -1
    

if ans == 2:
    if K <= 2:
        ans = -1
elif ans == 1:
    if K <= 1:
        ans = -1
else:
    pass
    
print(ans)