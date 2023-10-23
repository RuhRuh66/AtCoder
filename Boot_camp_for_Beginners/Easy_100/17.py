N = int(input())

v = list(map(int, input().split()))

v.sort()

from collections import deque

s = deque(v)

temp = s.popleft()
while s:
    temp = (temp+s.popleft())/2

print(temp)
    
    