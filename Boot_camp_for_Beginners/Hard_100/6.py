S = input()
T = input()

s = len(S)
t = len(T)

if s < t: 
    print('UNRESTORABLE')
    exit()
    
memo =[]

for i in range(s-t+1):
    flag = False
    for j in range(t):
        if S[i+j] != T[j] and S[i+j] != '?':
            flag = True
            break
    if flag == True:
        continue
    else:
        st = [S[k] if S[k] != '?' else 'a' for k in range(s)]
        for l in range(t):
            st[i+l] = T[l]
        memo.append(''.join(st))

if len(memo)==0:
    print('UNRESTORABLE')
else:
    memo.sort()
    print(memo[0])
    

      