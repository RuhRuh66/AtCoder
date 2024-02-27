S = input()

N = len(S)

ans = 0
ans += 2*(N-1)

for i in range (1, N-1):
    if S[i] == 'U':
        ans += N-1-i
        ans += 2*i
    else:
        ans += 2*(N-1-i)
        ans += i

print(ans)