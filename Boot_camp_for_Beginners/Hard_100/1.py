S = input()

N = len(S)

ans = [0] * N

cnt = 0

for i in range(N):
    if S[i] == 'R':
        cnt += 1
        
    else:
        ans[i-1] += (cnt+1) // 2
        ans[i] += cnt //2
        cnt = 0
        
S = list(reversed(S))

for i in range(N):
    if S[i] == 'R':
        S[i] = 'L'
    else:
        S[i] = 'R'
        
S = ''.join(S)

ans.reverse()

cnt = 0
for i in range(N):
    if S[i] == 'R':
        cnt += 1
        
    else:
        ans[i-1] += (cnt+1) // 2
        ans[i] += cnt //2
        cnt = 0
        
ans.reverse()

print(*ans)




    
    