S = input()

import re

s = re.compile(r'^(dream|dreamer|erase|eraser)*$')

a = s.search(S)
if a:
    print('YES')
else:
    print('NO')
    