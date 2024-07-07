S = input()

L = len(S)

ans = 0
for i in range(1<<(L-1)):
    temp = 0
    for j in range(L):
        if (i >> j) & 1 == 1:
            ans += temp*10+int(S[j])
            temp = 0
        else:
            temp = temp*10 + int(S[j])
    ans += temp
print(ans)

    