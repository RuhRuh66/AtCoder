A, B = map(int, input().split())
t = A*B

if A<B:
    A, B = B, A

r = 10**6
while r != 0:
    r = A % B
    A = B
    B = r
    
print(t//A)