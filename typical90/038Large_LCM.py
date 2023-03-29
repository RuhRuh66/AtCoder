A, B = map(int, input().split())

max = 10**18


def gcd(X, Y):
    if X > Y:
       X, Y = Y, X
    while X != 0:
        X, Y = Y % X, X
    return Y

k = gcd(A, B)

LCM = A * B // k
if LCM <= 10**18:
    print(LCM)
else:
    print('Large')
        
        
            
        
