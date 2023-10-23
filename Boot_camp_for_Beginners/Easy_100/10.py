N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

from collections import deque

cards = deque(A)

flag = 'Alice'

A = 0
B = 0

while cards:
    if flag == 'Alice':
        A += cards.popleft()
        flag = 'Bob'
    else:
        B += cards.popleft()
        flag = 'Alice'
        
print(A-B)