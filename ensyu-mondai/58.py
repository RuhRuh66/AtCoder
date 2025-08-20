N, X, Y = map(int, input().split())

if abs(X) + abs(Y) > N:
    print('No')
    exit()
    
else:
    if (N-(abs(X)+abs(Y))) % 2 == 0:
        print('Yes')
    else:
        print('No')
        
        
        
