N= int(input())
S1 = input()
S2 = input()

mod = 10**9+7
 
st = ''
flag = 1
for i in range(N-1):
    if S1[i+1] != S1[i]:
        if flag == 1:
            st += 'A'
        else:
            st += 'B'
            flag = 1
    else:
        flag -= 1
if flag == 1:
    st += 'A'
else:
    st += 'B'
        
l = len(st)
if st[0] == 'A':
    s = 3
else:
    s = 6
for i in range(1, l):
    if st[i-1] == 'A':
        s = (s*2) % mod
    else:
        if st[i] == 'A':
            s = s
        else:
            s = (s *3)  % mod
            
            
print(s)
        
        
        
     