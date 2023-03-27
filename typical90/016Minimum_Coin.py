N = int(input())

A, B, C = map(int, input().split())

ans = 10**10
for x in range(10000):
    if x*A > N:
        break
    for y in range(10000-x):
        balance = N-A*x-B*y
        if balance < 0:
            break
     
        if balance%C == 0:
            z =balance//C
            ans = min(z+x+y, ans)
          
print(ans)



