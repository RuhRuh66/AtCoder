S = input()
T = input()

S = list(S)
T = list(T)

for i in range(len(S)):
    if S[i] == T[0]:
        temp = S[i:] + S[:i]
        if temp == T:
            print('Yes')
            exit()
            
print('No')