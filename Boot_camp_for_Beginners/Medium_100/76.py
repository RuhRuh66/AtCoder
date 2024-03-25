N = int(input())
S = input()

w = S.count('W')
e = S.count('E')

final_ans = N

if S[0] == 'W':
    ans = e
else:
    ans = e-1

final_ans = min(final_ans, ans)
    
for i in range(1, N):
    if S[i] == 'W':
        if S[i-1] == 'W':
            ans += 1
        else:
            ans = ans
            
    else:
        if S[i-1] == 'W':
            ans = ans
        else:
            ans -= 1
    if final_ans > ans:
        final_ans = ans

    
print(final_ans)