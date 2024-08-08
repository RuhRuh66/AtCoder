def formula(x):
    n = (x+1)//2
    m = (x+1) % 2
    if m == 0:
        if n % 2 == 0:
            return 0
        else:
            return 1
    else:
        if n % 2 == 0:
            return x
        else:
            return x^1
        
    
A, B = map(int, input().split())

if A == 0:
    print(formula(B))
    exit()
else:
    print(formula(A-1) ^ formula(B))