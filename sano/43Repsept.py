K = int(input())

if K % 2 == 0:
    print(-1)
    exit()
    
a = 7%K
for i in range(1,K+1):
    if a == 0:
        print(i)
        exit()
    else:
        a = (a*10+7)%K
if a:
    print(-1)
    

    
    