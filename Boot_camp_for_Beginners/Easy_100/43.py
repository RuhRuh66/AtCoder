w = input()

A = list(w)

from collections import Counter

B = Counter(A)

a = all(B[i]%2==0 for i in B.keys())

if a:
    print('Yes')
else:
    print('No')