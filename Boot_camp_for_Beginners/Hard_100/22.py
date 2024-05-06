S = input()
T = input()

st  =[-1] * 26
go = [-1] * 26

for i in range(len(S)):
    a  = ord(S[i]) - ord('a')
    b = ord(T[i]) - ord('a')
    
    if st[a] != -1 or go[b] != -1:
        if st[a] !=b or go[b] !=a:
            print('No')
            exit()
            
    else:
        st[a] = b
        go[b] = a
print('Yes')
    