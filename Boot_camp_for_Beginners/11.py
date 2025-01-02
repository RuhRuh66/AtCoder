def factorization(N):
    pri = set()
    if N == 1:
        return pri
    while N % 2 == 0:
        pri.add(2)
        N //= 2
        
    c = 3
    while c*c <= N:
        while N % c == 0:
            pri.add(c)
            N //= c
        c += 2
        
    if N != 1:
        pri.add(N)
    
    return(pri)
        
A, B = map(int, input().split())

a = factorization(A)
b = factorization(B)

c = a & b


print(len(c)+1)
