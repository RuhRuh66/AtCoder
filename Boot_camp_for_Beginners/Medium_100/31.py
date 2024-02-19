N = int(input())
A = list(map(int, input().split()))

B = [''] * N
for i in range(N):
    temp = A[i] % 4
    if temp == 0:
        B[i] = 'f'
    elif temp == 2:
        B[i] = 'e'
    else:
        B[i] = 'o'
    
 
        
F = B.count('f')
O = B.count('o')
E = N-F-O

if F>= O:
    print('Yes')
    exit() 
if F != 0 and O-F == 1 and E == 0:
    print('Yes')
    exit()
    
print('No')
    
    