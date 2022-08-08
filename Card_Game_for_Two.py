N = int(input())
A = list(map(int, input().split()))

sorted_A = sorted(A, reverse=True)

from collections import deque

B = deque(sorted_A)

Alice = 0
Bob = 0
turn = 'Alice'

while B:
    if turn == 'Alice':
        Alice += B.popleft()
        turn = 'Bob'
    else:
        Bob += B.popleft()
        turn = 'Alice'

print(Alice-Bob)
        
        
        