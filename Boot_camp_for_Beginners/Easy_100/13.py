A, B, C = map(int, input().split())

if (A == B == C) and A % 2 == 0:
    print(-1)
    exit()
elif (A == B == C) and A % 2 == 1:
    print(0)
    exit()
    
else:    
    count = 0

    while (B+C)%2==0 and (C+A)%2 ==0 and (A+B)%2 == 0:
        A, B, C  = (B+C)//2, (C+A)//2, (A+B)//2
        count += 1
        
    print(count)


    