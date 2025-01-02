import re

a = re.compile(r'AB')

s = 'nBc'

if re.search(a, s):
    print('7')