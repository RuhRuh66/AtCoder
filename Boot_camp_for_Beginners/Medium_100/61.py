from collections import deque
S = input()
Q = int(input())

T = deque()
T.extend(S)

flag = True

for i in range(Q):
    temp = list(input().split())
    if temp[0] == '1':
        flag = not flag
    else:
        if temp[1] == '1':
            if flag:
                T.appendleft(temp[2])
            else:
                T.append(temp[2])
        else:
            if flag:
                T.append(temp[2])
            else:
                T.appendleft(temp[2])
                
ans = ''.join(T)
if flag:
    print(ans)
else:
    print(ans[::-1])