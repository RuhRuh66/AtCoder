N = int(input())

H = list(map(int, input().split()))


base = H[0]-1
H[0] -= 1

for i in range(1, N):
    if H[i] < base:
        print(('No'))
        exit()
        
    elif H[i] == base:
        pass
    elif H[i] > base:
        H[i] -= 1
        base = H[i]
        
for j in range(N-1):
    if H[j] > H[j+1]:
        print('No')
        exit()
        
print('Yes')    

    
     



    
