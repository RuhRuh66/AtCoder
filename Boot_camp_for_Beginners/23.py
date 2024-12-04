import re

t = re.compile(r'^(dream|dreamer|erase|eraser)*$')

S = str(input())

ans = re.match(t, S)

if ans:
    print('YES')
else:
    print('NO')