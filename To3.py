N = int(input())


N = str(N)
k = len(N)
list_N = list(N)

n = [int(i)%3 for i in list_N]

m = sum(n) % 3


ans = 0

if m == 0:
    ans = 0
    
elif m == 1:
    if n.count(1) >= 1:
        ans = 1
    elif n.count(2) >=2:
        ans = 2

else:
    if n.count(2) >=1:
        ans = 1
    elif n.count(1) >= 2:
        ans = 2
        
if k - ans >= 1:
    print(ans)
else:
    print(-1)
        
