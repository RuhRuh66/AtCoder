A, B, K = map(int, input().split())

l = B-A+1



ans = []
if l > 2*K:
    for i in range(K):
        ans.append(A+i)
        ans.append(B-i)
    
    ans.sort()
    
else:
    ans = [i for i in range(A, B+1)]
   

for j in ans:
    print(j)
