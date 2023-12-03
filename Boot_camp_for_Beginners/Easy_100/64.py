O = input()
E = input()

from collections import deque
O = deque(list(O))
E = deque(list(E))

A =[]
flag = True
while O or E:
    if flag:
        A.append(O.popleft())
        flag = False
    else:
        A.append(E.popleft())
        flag = True

print(*A, sep='')

    

