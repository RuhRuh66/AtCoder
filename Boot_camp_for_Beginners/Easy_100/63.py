N = int(input())
A = list(map(int, input().split()))

s = 1
count = 0
for i in range(N):
    if s != A[i]:
        count += 1
    else:
        s += 1

print(count if not count == N else -1)
        
    

    

    
        
        
        
    