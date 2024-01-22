N = str(input())

import re

s = re.compile(r'(^[1-9])9*$')

result = re.search(s, N)

if result:
    print(int(N[0]) + (len(N)-1)*9)

else:
    print(int(N[0]) + (len(N)-1)*9-1)