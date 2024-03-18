from collections import deque

A = input()
B = input()
C = input()

Ad = deque()
Bd = deque()
Cd = deque()

Ad.extend(A)
Bd.extend(B)
Cd.extend(C)

Ad.append('x')
Bd.append('x')
Cd.append('x')

now_player = 'A'
now_card = ''

while now_card != 'x':
    if now_player =='A':
        now_stack = Ad
    elif now_player == 'B':
        now_stack = Bd
    else:
        now_stack = Cd
            
    now_card = now_stack.popleft()
    if now_card == 'a':
        now_player = 'A'
    elif now_card == 'b':
        now_player = 'B'
    elif now_card == 'c':
        now_player = 'C'
    else:
        break
print(now_player)
