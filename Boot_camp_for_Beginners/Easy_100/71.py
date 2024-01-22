N, L = map(int, input().split())
ans = []
for i in range(N):
    temp = input()
    ans.append(temp)
    
ans.sort()

print(''.join(ans))
    

    