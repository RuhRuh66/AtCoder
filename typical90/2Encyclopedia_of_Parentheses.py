def isvalid(s):
    count = 0
    for i in s:
        if i =='(':
            count += 1
        else:
            count -= 1
            
        if count < 0:
            return False
   
    return (count==0)

from itertools import product
N = int(input())
for s in product(['(', ')'], repeat=N):
    if isvalid(s):
        print(*s, sep='')