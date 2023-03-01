S = list(input())
Q = int(input())
query = []
for i in range(Q):
    temp = list(input().split())
    query.append(temp)
    
    
from collections import deque
S = deque(S)   
  

reverse = False
for i in query:
    if i[0] == '1':
        reverse = not reverse
        
    else:
        if i[1] == '1':
            if reverse == False:
                S.appendleft(i[2])
            else:
                S.append(i[2])
        else:
            if reverse == True:
                S.appendleft(i[2])
            else:
                S.append(i[2])

                
S = list(S)
if reverse == False:
    print(''.join(S))
else:
    print(''.join(S[::-1]))
    