N = int(input())
B = list(map(int, input().split()))



ans = []
for i in range(N):
    C = list(enumerate(B, start=1))
    for i, j in reversed(C):
        if i == j:
            del B[i-1]
            ans.append(i)
            break

if B:
    print(-1)
    
else:  
    for i in reversed(ans):
        print(i)
        
        

