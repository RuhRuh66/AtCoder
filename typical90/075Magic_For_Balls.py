N = int(input())

count = 0

p = 2
while p*p <= N:
    while N % p == 0:
        count += 1
        N //= p
    p += 1
    
if N >1:
    count += 1
    


if count == 1:
    print(0)
else:
    ans = 0
    while 2 ** ans < count:
        ans += 1
        
    print(ans)
    


    