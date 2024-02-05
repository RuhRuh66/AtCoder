N, M = map(int, input().split())

ans = [-1] * N

for i in range(M):
    s, c = map(int, input().split())
    if N == 1:
        if ans[s-1] != -1:
            if ans[s-1] != c:
                print(-1)
                exit()
            else:
                continue
        else:
            ans[s-1] = c
    else:
        if s == 1 and c == 0:
            print(-1)
            exit()
        else:
            if ans[s-1] != -1:
                if ans[s-1] != c:
                    print(-1)
                    exit()
                else:
                    continue
            else:
                ans[s-1] = c
                
                
if ans[0] == -1:
    if len(ans) != 1:
        ans[0] = 1
    else:
        ans[0] = 0
    
ans = ['0' if i == -1 else str(i) for i in ans]

print(int(''.join(ans)))
    
    
    