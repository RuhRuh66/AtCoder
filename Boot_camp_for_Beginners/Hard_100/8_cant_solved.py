n = int(input())

if n%2 == 1:
    print(0)
    exit()
    
else:
    X = 0
    n //= 2
    while n > 0:
        X += n//5
        n //= 5
        
print(X)
        
    