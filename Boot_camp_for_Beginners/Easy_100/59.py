S = input()

import re

a = re.compile(r'^A[a-z]+C[a-z]+$')

ans = re.match(a, S)

if ans:
    print('AC')
else:
    print('WA')