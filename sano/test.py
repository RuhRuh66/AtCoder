import re
S = input()

p = r'^\w+\@\w+\.\w{1,4}$'

if re.search(p, S):
    print('Yes')
else:
    print('No')