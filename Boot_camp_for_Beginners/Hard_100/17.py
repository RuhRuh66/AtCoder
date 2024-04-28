import re

AB = re.compile(r'^B.*A$')
A = re.compile(r'^[^B].*A$')
B = re.compile(r'^B.*[^A]$')

c = 0
ab = 0
a = 0
b = 0

N = int(input())
for i in range(N):
    s = input()
    c += s.count('AB')
    if re.match(AB, s):
        ab += 1
    elif re.match(A, s):
        a += 1
    elif re.match(B, s):
        b += 1
    else:
        continue
    


ans = c
if ab == 0:
    if (a or b) == 0:
        ans = c
    else:
        ans += min(a, b)
        
else:
    if (a or b) == 0:
        if a == 0 and b == 0:
            ans += ab-1
        else:
            ans += ab
        
    else:
        ans += (ab-1 + 2 + min(a-1, b-1))
        
print(ans)