N = int(input())

import re 

a = re.compile(r'^[^B].*A$') 
b = re.compile(r'^B.*[^A]$') 
ba = re.compile(r'^B.*A$')  


ac = 0
bc = 0
bac = 0
abc = 0



for i in range(N):
    s = str(input())
    
    abc += s.count('AB')
    
    if re.match(a, s):
        ac += 1
        
    if re.match(b, s):
        bc += 1
    if re.match(ba, s):
        bac += 1

    
if ac+bc == 0:
    if bac == 0:
        ans = abc
    else:
        ans = abc + bac-1
    
else:
    ans = abc + min(ac, bc) + bac

print(ans)