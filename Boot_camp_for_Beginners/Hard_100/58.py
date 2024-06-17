N = int(input())

if N == 2:
    print(0)
    exit()
    

ans = 0
a = 1
while a*a <N:
    if (N-a) % a == 0 and (N-a)//a != a:
        ans += (N-a)//a
    a += 1

        
print(ans)
    