S = input()
Q = int(input())

from collections import deque
T = deque()
T.extend(S)



Flag = True
for i in range(Q):
    temp = input()
    if len(temp) == 1:
        Flag = not Flag
    else:
        t, f, c = temp.split()       
        if f == '1':
            if Flag:
                T.appendleft(c) 
            else:
                T.append(c)
        else:
            if Flag:
                T.append(c) 
            else:
                T.appendleft(c) 

if Flag:
    print(''.join(T))
    
else:
    print(''.join(T)[::-1])
        