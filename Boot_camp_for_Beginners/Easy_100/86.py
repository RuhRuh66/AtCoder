import re

pat = re.compile(r'^(1+)([2-9])')

S = input()
K = int(input())

res = pat.match(S)
if res:
    a = len(res.group(1))
    b = res.group(2)

    if K <= a:
        print(1)
    else:
        print(int(b))
else:
    print(S[0])

