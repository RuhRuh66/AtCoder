N, M, K = map(int, input().split())

ans = set()
for x in range(N+1):
    for y in range(M+1):
        temp = M*x + N*y - 2*x*y
        ans.add(temp)
        
if K in ans:
    print('Yes')
else:
    print('No')