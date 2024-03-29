S = input()

L = len(S)
T = list(S)

al = [chr(i) for i in range(97, 123)]

if L < 26:
    for i in range(26):
        if al[i] not in T:
            S += al[i]
            print(S)
            exit()
else:
    for i in range(25, -1, -1):
        sa = S[i]
        for j in range(26):
            c = al[j]
            if sa < c and c not in S[:i]:
                print(S[:i] + c)
                exit()
        
print(-1)  

