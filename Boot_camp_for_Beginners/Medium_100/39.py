K, A, B = map(int, input().split())

if A >= B-2:
    ans = K+1
    print(ans)
    exit()
    
else:
    if K < A+1:
        ans = K+1
        print(ans)
        exit()
        
    else:
        if (K-(A+1)) % 2 == 0:
            ans = (((K-(A+1))//2)+1)*B - ((K-(A+1))//2) * A
        else:
            ans = (((K-(A+1))//2)+1)*B - ((K-(A+1))//2) * A + 1
            

    print(ans)