N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

from collections import defaultdict
a = defaultdict(int)
b = defaultdict(int)
c = defaultdict(int)

for i in A:
    amari = i%46
    a[amari] += 1
    
for i in B:
    amari = i%46
    b[amari] += 1

for i in C:
    amari = i%46
    c[amari] += 1

ans = 0
for x in a:
    for y in b:
        for z in c:
            if (x+y+z)%46 ==0:
                ans += a[x]*b[y]*c[z]
print(ans)
                 