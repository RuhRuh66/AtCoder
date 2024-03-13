N, A, B, C, D = map(int, input().split())
S = '0' + input()

rock2 = 0
room3 = 0

if C<D:
    for i in range(A, D-2):
        if S[i+1] == '#' and S[i+2] =='#':
            rock2 = 1
            break
    if rock2 == 1:
        print('No')
    else:
        print('Yes')
    
else:
    for x in range(B, D+1):
        if S[x-1] == '.' and S[x] == '.' and S[x+1] == '.':
            room3 = 1
    for i in range(A, C-2):
        if S[i+1] == '#' and S[i+2] == '#':
            rock2 = 1
            
    if room3:
        if rock2:
            print('No')
        else:
            print('Yes')
    else:
        print('No')

        



    

    

         

