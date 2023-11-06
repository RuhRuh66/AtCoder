import re

A, B = map(int, input().split())
S = input()

pat = re.compile('[0-9]'*A + '-' + '[0-9]'*B)

s = re.match(pat, S)

if s:
    print('Yes')
else:
    print('No')



    