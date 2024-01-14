S = sorted(list(map(int, input().split())), reverse=True)

if S[0] %2 == 0:
    ans = 0
else:
    ans = S[1] * S[2]
    
print(ans)

