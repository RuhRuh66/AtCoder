N, M = map(int, input().split())

if N == 1:
    if M == 1:
        ans = 1
    elif M == 2:
        ans = 0
    else:
        ans = M-2
        
elif N == 2:
    ans = 0
    
else:
    if M == 1:
        ans = N-2
    elif M == 2:
        ans = 0
    else:
        ans = (N-2) * (M-2)
        

print(ans)
    

    
    
